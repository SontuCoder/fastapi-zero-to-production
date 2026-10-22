from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(
    title="My FastAPI Application",
    description=("This is a sample FastAPI application."
                " It demonstrates how to create a simple API with FastAPI."),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    )

@app.get("/")
async def read_root(id : int = 1):
    """First Text route of the FastAPI application."""
    return {"Hello": "World"}

@app.get("/debug/request-info",
        summary="Get request information",
        description=("This route returns information about the incoming request, including method, URL, headers, client IP, path parameters, and query parameters."),
        tags=["Debug", "Request Info"],
        response_description="A JSON object containing request information.",
        deprecated=False,

)
async def request_info(request: Request):
    """Debug route to get request information."""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": request.client.host if request.client else None,
        "path_params": dict(request.path_params),
        "query_params": dict(request.query_params),
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

"""
// Life Cycle of a FastAPI Application
1. Client sends a HTTP request to the FastAPI application.
2. Unicorn ASGI server (raw bytes)
3. STARLET route matching
4. Middleware processing
5. Dependency injection
6. Pydantic model validation
7. Request handler function
8. Response Validation pydantic model
9. Middleware processing (response)
10. Uvicorn ASGI server (raw bytes)
"""
