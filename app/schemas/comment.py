from pydantic import BaseModel


class CommentCreate(BaseModel):
    content: str
    user_id: int
    article_id: int


class CommentResponse(BaseModel):
    id: int
    content: str
    user_id: int
    article_id: int

    class Config:
        from_attributes = True