from fastapi import FastAPI, HTTPException, Query
import uvicorn
from data import chaies



app = FastAPI(
    title="Chai Menu",
    description=("A Read Manu of Chai Stall." 
                " Hi All"),
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

@app.get("/menu",
        summary="Get all Items",
        description=("This route returns list of chaies."),
        tags=["Items"],
        deprecated=False
)
def all_chaies(category: str | None = Query(None)):
    """if 'Category isn't present then this Route return all chies, else return category wise"""
    if not category:
        return {
            "message": "These are our all chaies",
            "total_chaies": len(chaies),
            "chaies" : chaies
        }

    filtered_chai = [chai for chai in chaies if category in chai["categories"]]
    if len(filtered_chai):
        return {
                    "message": f"These are our all chaies in this category '{category}'",
                    "total_chaies": len(filtered_chai),
                    "chaies" : filtered_chai
                }
    return {
        "message": f"These are no chai in this category '{category}'",
        "total_chaies": len(filtered_chai),
        "chaies" : filtered_chai
    }

@app.get("/menu/{id}",
        summary="Get Item by id",
        description=("This route returns chai by id."),
        tags=["Item"],
        deprecated=False
)
def get_chai_id(id: int):
    """Return Chai by id"""
    filtered_chai = next((chai for chai in chaies if chai["id"] == id), None)
    if filtered_chai is None:
        raise HTTPException(
            status_code=404,
            detail="Chai not found"
        )
    return {
        "message": "This is the chai",
        "chai" : filtered_chai
    }



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)