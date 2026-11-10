from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from enum import Enum
from pydantic import field_validator


class BookCategory(Enum):
    Cpp = "c++"
    Python = "python"
    Java = "java"
    Others = "others"


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    category: BookCategory = Field(nullable=False, default=BookCategory.Others)
    owners: list["User"] = Relationship(back_populates="own_books", link_model=UserBook)
    borrowers: list["User"] = Relationship(back_populates="borrow_books", link_model=BorrowBook)
    created_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_on: datetime | None = Field(default=None, nullable=True)

class BookCreate(SQLModel):
    name: str
    category: BookCategory = BookCategory.Others
    owner_ids: list[int]
    
    @field_validator("name")
    @classmethod
    def check_name(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError("Name should not be blank")
        return value

from user_model import User
from user_book_model import UserBook
from borrow_book_model import BorrowBook
Book.model_rebuild()
