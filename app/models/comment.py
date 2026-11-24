from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))

    article = relationship("Article", back_populates="comments")