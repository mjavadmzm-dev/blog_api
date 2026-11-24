from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..db.database import get_db
from ..models.article import Article
from ..schemas.article import ArticleCreate, ArticleResponse

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("/", response_model=ArticleResponse)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    new_article = Article(**article.model_dump())

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


@router.get("/", response_model=list[ArticleResponse])
def get_articles(db: Session = Depends(get_db)):
    articles = db.scalars(select(Article)).all()
    return articles