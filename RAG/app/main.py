from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
import uvicorn
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class Requestbody(BaseModel):
    question: str

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

API_KEY=os.getenv("OPENAI_API_KEY")

open_ai = OpenAI(api_key=API_KEY) 


vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="First_RAG_Project",
    url="http://localhost:6333/"
)

@app.post("/query")
def get_query(req:Requestbody):
    question = req.question
    if not question.strip():
        raise HTTPException(
            status_code=400,
            detail="Please send a question"
        )

    response = vector_db.similarity_search(question)

    context = "".join([res.page_content for res in response])
    SYSTEM_Prompt = f"""
You are a helpful assistant that answer questions based on the provided context. If the context does not contain the answer, respond with "I dont't know."
context: {context}
"""

    ai_result = open_ai.chat.completions.create(model="gpt-5", messages=[
        {"role":"system", "content": SYSTEM_Prompt},
        {"role":"user", "content": question}
    ], max_completion_tokens=2000)
    return ai_result

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

    