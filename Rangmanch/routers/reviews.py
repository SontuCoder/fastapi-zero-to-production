from fastapi import APIRouter


router = APIRouter(prefix="/review", tags=["Reviews"])

@router.get("/")