from sqlalchemy import Column, ForeignKey, Integer, String, Text

from blog.models.database import db


class Article(db.Model):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    text = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Post %r>" % self.title
