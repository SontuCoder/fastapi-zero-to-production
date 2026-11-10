from sqlmodel import SQLModel, Field

class BorrowBook(SQLModel, table=True):
    user_id: int = Field(
        foreign_key="user.id",
        primary_key=True
    )

    book_id: int = Field(
        foreign_key="book.id",
        primary_key=True
    )
