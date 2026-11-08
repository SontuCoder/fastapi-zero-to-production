from pydantic import BaseModel, field_validator, ConfigDict
import re

class Customer_add(BaseModel):
    name: str
    location: str
    number: str

    @field_validator("number")
    @classmethod
    def number_validate(cls, value):
        if len(value) != 10:
            raise ValueError("Number should be length of 10")
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Number must contain exactly 10 digits")
        return value

    @field_validator("name", "location")
    @classmethod
    def name_location_validate(cls, value:str):
        if not value.strip():
            raise ValueError("Name and location should not blank")
        return value

class Customer(BaseModel):
    id: int
    name: str
    location: str
    number: str

class Customer_Created(BaseModel):
    message: str
    customer: Customer

class Customers(BaseModel):
    customers: list[Customer]

class Delivery_Boy_add(BaseModel):
    name: str
    number: str

    @field_validator("number")
    @classmethod
    def number_validate(cls, value):
        if len(value) != 10:
            raise ValueError("Number should be length of 10")
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Number must contain exactly 10 digits")
        return value

    @field_validator("name")
    @classmethod
    def name_location_validate(cls, value:str):
        if not value.strip():
            raise ValueError("Name should not blank")
        return value

class Delivery_Boy(BaseModel):
    id: int
    name: str
    number: str


class Delivery_Boy_Created(BaseModel):
    message: str
    delivery_boy: Delivery_Boy

class Delivery_Boys(BaseModel):
    delivery_boys: list[Delivery_Boy]

class Kitchen_add(BaseModel):
    name: str
    number: str

    @field_validator("number")
    @classmethod
    def number_validate(cls, value):
        if len(value) != 10:
            raise ValueError("Number should be length of 10")
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Number must contain exactly 10 digits")
        return value

    @field_validator("name")
    @classmethod
    def name_location_validate(cls, value:str):
        if not value.strip():
            raise ValueError("Name should not blank")
        return value

class Delivery_Boy(BaseModel):
    id: int
    name: str
    number: str


class Delivery_Boy_Created(BaseModel):
    message: str
    delivery_boy: Delivery_Boy

class Delivery_Boys(BaseModel):
    delivery_boys: list[Delivery_Boy]

