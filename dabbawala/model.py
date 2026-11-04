from sqlalchemy.orm import Mapped, mapped_column, relationship
from db_config import Base
from sqlalchemy import String, CheckConstraint, Index



class Customer(Base):
    __tablename__ = "Customer"

    __table_args__ = ({
        "comment": "Table for storing user details."
    },(
        CheckConstraint(
            "number ~ '^[0-9]{10}$'",
            name="number_match"
        )
    ),(
        Index(
            "idx_number", "number"
        )
    ))

    id: Mapped[int] = mapped_column(primary_key=True, default=None)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False)
    number: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)


class 