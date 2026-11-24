from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..db.database import get_db
from ..models.category import Category
from ..schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**category.model_dump())

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    categories = db.scalars(select(Category)).all()
    return categories