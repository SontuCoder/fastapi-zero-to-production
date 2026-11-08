from fastapi import FastAPI
from contextlib import asynccontextmanager
from db_config import create_tables
import uvicorn
from routes import order_routes, customer_routes, delivery_routes

@asynccontextmanager
async def life_span(app: FastAPI):
    create_tables()
    print("==========DB table created==============")
    yield
    print("==========App shut down===============")

app = FastAPI(
    lifespan=life_span,
    title="Dabbawala APP",
    description="An food booking App."
)

@app.get("/")
def check_helth():
    return{
        "message":"App is ok"
    }

app.include_router(order_routes)
app.include_router(customer_routes)
app.include_router(delivery_routes)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host="127.0.0.1")
