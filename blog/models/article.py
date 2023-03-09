from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import relationship

from blog.models.database import db


class Article(db.Model):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    text = Column(Text)
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="articles")

    def __repr__(self):
        return "<Post %r>" % self.title
