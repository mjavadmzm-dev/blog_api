from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    email: Mapped[str] = mapped_column(String(150), unique=True)
    password: Mapped[str] = mapped_column(String(255))

    articles = relationship("Article", back_populates="user")