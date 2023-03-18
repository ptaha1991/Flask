from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api

from blog.api.author import AuthorDetail, AuthorList
from blog.api.tag import TagDetail, TagList
from blog.api.user import UserDetail, UserList


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        # Declaring tags list with their descriptions,
        # so API gets organized into groups. it's optional.
        tags={
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Article": "Article API",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(
        app,
        plugins=[
            api_spec_plugin,
        ],
    )
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")
    api.route(TagList, "article_list", "/api/articles/", tag="Article")
    api.route(TagDetail, "article_detail", "/api/articles/<int:id>/", tag="Article")
