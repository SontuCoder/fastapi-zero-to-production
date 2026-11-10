from sqlmodel import SQLModel, Field, Relationship
from pydantic import field_validator
from datetime import datetime, timezone
from typing import Optional
import re


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    number: int = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)
    own_books: list["Book"] = Relationship(back_populates="owners", link_model=UserBook)
    borrow_books: list["Book"] = Relationship(back_populates="borrowers", link_model=BorrowBook)
    created_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_on: datetime | None = Field(default=None, nullable=True)

class UserCreate(SQLModel):
    name: str
    number: str
    password: str

    @field_validator("name")
    @classmethod
    def check_name(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("Name should not be blank")

        return value

    @field_validator("number")
    @classmethod
    def check_number(cls, value: str):

        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Number must contain exactly 10 digits")

        return value

    @field_validator("password")
    @classmethod
    def check_password(cls, value: str):

        checks = {
            "Minimum 8 characters": lambda v: len(v) >= 8,
            "At least 1 Capital letter": lambda v: bool(re.search(r"[A-Z]", v)),
            "At least 1 Number": lambda v: bool(re.search(r"\d", v)),
            "At least 1 Special character": lambda v: bool(
                re.search(r"[^A-Za-z0-9\s/]", v)
            ),
            "No Spaces": lambda v: not bool(re.search(r"\s", v)),
            "No Slash": lambda v: "/" not in v
        }

        errors = []

        for condition, check in checks.items():
            if not check(value):
                errors.append(condition)

        if errors:
            raise ValueError(
                "Password validation failed: " + ", ".join(errors)
            )

        return value



from books_model import Book
from user_book_model import UserBook
from borrow_book_model import BorrowBook
User.model_rebuild()

