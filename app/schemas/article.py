from pydantic import BaseModel


class ArticleCreate(BaseModel):
    title: str
    content: str
    user_id: int
    category_id: int


class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    category_id: int

    class Config:
        from_attributes = True