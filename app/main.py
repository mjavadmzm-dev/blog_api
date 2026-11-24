from fastapi import FastAPI

from app.api import comments

from .api import articles, categories
from .db.database import engine, Base

from .models.user import User
from .models.category import Category
from .models.article import Article
from .models.comment import Comment

from .api import users


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API")


app.include_router(users.router)
app.include_router(categories.router)
app.include_router(articles.router)
app.include_router(comments.router)


@app.get("/")
def home():
    return {"message": "Welcome to Blog API"}