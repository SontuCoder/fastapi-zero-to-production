from fastapi import APIRouter, Depends, HTTPException, status, Query
from model import Reviews, ReviewCreate, ReviewRead, ReviewUpdate
from db_config import get_session
from sqlmodel import Session, select, func
from typing import Optional



router = APIRouter(prefix="/review", tags=["Reviews"])

@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):
    review_date = Reviews(**review.model_dump())
    session.add(review_date)
    session.commit()
    session.refresh(review_date)
    return review_date

@router.get("", response_model=list[ReviewRead])
def get_all_reviews(
    id: int | None = Query(None, description="Review Id"),
    play_name:str | None= Query(None, description="Filter by play name"),
    offset:int = Query(0, ge=0, description="Offset"),
    limit:int = Query(5, ge=1, le=10, description="Limit"),
    revier_name:str | None= Query(None, description="Filter by reviewer name"),
    session: Session = Depends(get_session)
):
    query = select(Reviews)
    if play_name:
        query = query.where(Reviews.play_name == play_name)

    if id is not None:
        query = query.where(Reviews.id == id)

    if revier_name:
        query = query.where(Reviews.reviewer_name == revier_name)

    query = query.offset(offset).limit(limit)
    reviews = session.exec(query).all()
    return reviews


@router.patch("/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: int,
    review: ReviewUpdate,
    session: Session = Depends(get_session)
):
    # 1. Fetch existing review
    review_db = session.get(Reviews, review_id)

    if review_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )

    # 2. Get only fields provided by the client
    update_data = review.model_dump(exclude_unset=True)

    # 3. Check whether any fields were provided
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No details provided for update"
        )

    # 4. Prevent NULL values for non-nullable fields
    if any(value is None for value in update_data.values()):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Review fields cannot be null"
        )

    # 5. Update only the supplied fields
    for key, value in update_data.items():
        setattr(review_db, key, value)

    # 6. Save changes
    session.commit()
    session.refresh(review_db)

    return review_db




