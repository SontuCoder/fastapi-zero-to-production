from fastapi.responses import JSONResponse
from fastapi import Request


class PinCodeNotFound(Exception):
    def __init__(self, pincode:str):
        self.pincode = pincode

class InvalidPinCode(Exception):
    def __init__(self, pincode:str, reason: str = "Invalid formate"):
        self.pincode = pincode
        self.reason = reason

async def pincode_not_found_handler(request: Request, exception: PinCodeNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "pincode": exception.pincode,
            "error": "pincode_not_found",
            "message": f"No location for pincode : {exception.pincode}",
        }
    )

async def invalid_pincode_handler(request: Request, exception: InvalidPinCode):
    return JSONResponse(
        status_code=400,
        content={
            "pincode": exception.pincode,
            "error": "invalid_pincode",
            "message": f"Pincode : {exception.pincode} is invalid : {exception.reason}",
        }
    )