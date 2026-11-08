from fastapi import APIRouter, Depends, HTTPException
from data_structure import Customer_add, Customer_Created, Customers
from db_config import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session
from dependency import check_customer_present
from model import Customer


route = APIRouter(prefix="/customer", tags=["Customer"])

@route.post("", response_model=Customer_Created, status_code=201)
def add_customer(
    customer: Customer_add,
    session: Session = Depends(get_db),
    num_exist: bool = Depends(check_customer_present)
):
    if num_exist:
        raise HTTPException(
            status_code=409,
            detail="Customer already exists in DB"
        )

    new_data = Customer(**customer.model_dump())

    session.add(new_data)
    session.commit()
    session.refresh(new_data)

    return {
        "message": "New customer created",
        "customer": new_data
    }


@route.get("",response_model=Customers, status_code=200)
def get_customers(session:Session=Depends(get_db)):
    query = select(Customer)
    data = session.execute(query).scalars().all()
    return {
        "customers" : data
    }

