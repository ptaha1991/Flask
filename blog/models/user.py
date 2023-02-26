from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from blog.models.database import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    articles = relationship("Article")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"
