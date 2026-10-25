from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    pincode: str

    # pincode validate in this model
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be exactly 6 digits")
        return value


class LocationResponse(BaseModel):
    pincode: str
    city: str
    