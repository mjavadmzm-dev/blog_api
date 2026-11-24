from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    user = relationship("User", back_populates="articles")
    category = relationship("Category", back_populates="articles")
    comments = relationship("Comment", back_populates="article")