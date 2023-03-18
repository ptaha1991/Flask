from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.models import Author
from blog.models.database import db
from blog.schemas import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }

    
class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }