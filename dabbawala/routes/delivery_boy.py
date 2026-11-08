from fastapi import APIRouter, Depends, HTTPException
from data_structure import Delivery_Boy_add, Delivery_Boy_Created, Delivery_Boys
from db_config import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session
from dependency import check_delivery_present
from model import DeliveryBoy

route = APIRouter(prefix="/delivery-boy", tags=["Delivery Boy"])

@route.post("", response_model=Delivery_Boy_Created, status_code=201)
def add_boy(
    delivery_boy: Delivery_Boy_add,
    session: Session = Depends(get_db),
    num_exist: bool = Depends(check_delivery_present)
):
    
    if num_exist:
        raise HTTPException(
            status_code=409,
            detail="Delivery Boy already exists in DB"
        )

    new_data = DeliveryBoy(**delivery_boy.model_dump())

    session.add(new_data)
    session.commit()
    session.refresh(new_data)

    return {
        "message": "New delivery boy created",
        "delivery_boy": new_data
    }


@route.get("",response_model=Delivery_Boys, status_code=200)
def get_boys(session:Session=Depends(get_db)):
    query = select(DeliveryBoy)
    data = session.execute(query).scalars().all()
    return {
        "delivery_boys" : data
    }

