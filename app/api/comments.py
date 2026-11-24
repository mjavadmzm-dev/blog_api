from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..db.database import get_db
from ..models.comment import Comment
from ..schemas.comment import CommentCreate, CommentResponse

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    new_comment = Comment(**comment.model_dump())

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


@router.get("/", response_model=list[CommentResponse])
def get_comments(db: Session = Depends(get_db)):
    comments = db.scalars(select(Comment)).all()
    return comments