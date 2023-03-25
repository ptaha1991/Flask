from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.models import Article, Author
from blog.models.database import db
from blog.schemas import AuthorSchema


class AuthorListEvents(EventsResource):
    def event_get_count(self, *args, **kwargs):
        return {'count': Author.query.count()}


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter(Article.author_id == kwargs["id"]).count()}


class AuthorList(ResourceList):
    events = AuthorListEvents
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }

    
class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }