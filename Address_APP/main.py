from fastapi import FastAPI
import uvicorn
from exceptions import (
    PinCodeNotFound,
    pincode_not_found_handler,
    InvalidPinCode,
    invalid_pincode_handler
)
from model import PincodeRequest, LocationResponse
from data import data

app = FastAPI(
    title="Address APP",
    description=("An address App." 
                " where we fill pincode and city automaticaly comes."),
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.add_exception_handler(PinCodeNotFound, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCode, invalid_pincode_handler)


@app.get("/address",
    response_model= LocationResponse,
    summary="Get address",
    description=("This route returns address."),
    tags=["Items"],
    deprecated=False
)
def get_address(id:PincodeRequest):
    if not id.pincode in data.keys():
        raise PinCodeNotFound(id.pincode)
    else:
        return {
            "pincode" : id.pincode,
            "city": data[id.pincode]["city"]
        }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host="127.0.0.1")
    