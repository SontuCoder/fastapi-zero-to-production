from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from model import Customer, DeliveryBoy
from data_structure import Customer_add, Delivery_Boy_add
from db_config import get_db


def check_customer_present(
    customer: Customer_add,
    db: Session = Depends(get_db)
) -> bool:

    query = select(Customer).where(
        Customer.number == customer.number
    )

    cust = db.execute(query).scalars().first()

    return cust is not None

def check_delivery_present(
    delivery_boy: Delivery_Boy_add,
    db: Session = Depends(get_db)
) -> bool:

    query = select(DeliveryBoy).where(
        DeliveryBoy.number == delivery_boy.number
    )

    boy = db.execute(query).scalars().first()

    return boy is not None