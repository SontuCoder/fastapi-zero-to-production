from sqlalchemy.orm import Mapped, mapped_column, relationship
from db_config import Base
from sqlalchemy import String, CheckConstraint, Index, Text, ForeignKey, DateTime



class Customer(Base):
    __tablename__ = "customer"

    __table_args__ = ({
        "comment": "Table for storing user details."
    },(
        CheckConstraint(
            "number ~ '^[0-9]{10}$'",
            name="number_match"
        )
    ))

    id: Mapped[int] = mapped_column(primary_key=True, default=None)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False)
    number: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)


class DeliveryBoy(Base):
    __tablename__ = "delivery_boy"

    __table_args__ = ({
        "comment": "Table for storing delivery boy details."
    },(
        CheckConstraint(
            "number ~ '^[0-9]{10}$'",
            name="number_match"
        )
    ))

    id: Mapped[int] = mapped_column(primary_key=True, default=None)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    number: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)


class Kitchen(Base):
    __tablename__ = "kitchen"
    __table_args__ = {
        "comment": "Table for storing kitchen details."
    }

    id: Mapped[int] = mapped_column(primary_key=True, default=None)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    owner: Mapped[str] = mapped_column(String(100), nullable=False)
    dishes: Mapped[str] = mapped_column(Text,nullable=True)

class Order(Base):
    __tablename__ = "orders"
    __table_args__ = ({
        "comment" : "Table for storing order details." 
    },(
       CheckConstraint(
            "status IN ('PLACED', 'CONFIRMED', 'PREPARING', "
            "'READY', 'OUT_FOR_DELIVERY', 'DELIVERED', 'CANCELLED')",
            name="ck_orders_status",
        ))

    id: Mapped[int] = mapped_column(primary_key=True, default=None)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"), nullable=False)
    dabbawala_id: Mapped[int|None] = mapped_column(ForeignKey("delivery_boy.id"))
    kitchen_id: Mapped[int] = mapped_column(ForeignKey("kitchen.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default="PLACED")
    dished: Mapped[str] = mapped_column(String(100), nullable=False)
    ordered_on: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    delivery_on: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    customer: Mapped["Customer"] = relationship()
    delivary: Mapped["DeliveryBoy"] = relationship()
    kitchen: Mapped["Kitchen"] = relationship()
    



