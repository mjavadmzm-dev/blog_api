from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(255))

    articles = relationship("Article", back_populates="category")