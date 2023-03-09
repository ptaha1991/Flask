from flask_login import UserMixin
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from blog.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    email = Column(String(255), unique=True)
    password = Column(db.String(255))
    is_staff = Column(Boolean, nullable=False, default=False)
    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

    def __init__(self, email, password, first_name, last_name, username, is_staff):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.is_staff = is_staff
