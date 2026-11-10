from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional
from enum import Enum


class BookCategory(Enum):
    Cpp = "c++"
    Python = "python"
    Java = "java"
    Others = "others"


class Book(SQLModel, table=True):
    
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, index=True)
    edition: int = Field(nullable=False, default=0, ge=0)
    category: BookCategory = Field(nullable=False, default=BookCategory.Others)
    owner_id: list[int] = Field(foreign_key="user.id")
    owner: list["User"] = Relationship(back_populates="own_books")
    borrowers: list[int] = Field(foreign_key="user.id")
    created_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_on: datetime | None = Field(default=None, nullable=True)


from user_model import User
Book.model_rebuild()
