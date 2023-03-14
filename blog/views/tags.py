from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import Tag

tags_app = Blueprint("tags_app", __name__)


@tags_app.route("/", endpoint="list")
def tags_list():
    tags = Tag.query.all()
    return render_template("tags/list.html", tags=tags)


@tags_app.route("/<int:tag_id>/", endpoint="details")
def tag_details(tag_id: int):
    tag = Tag.query.filter_by(id=tag_id).one_or_none()
    if tag is None:
        raise NotFound(f"Tag #{tag_id} doesn't exist!")
    return render_template("tags/details.html", tag=tag)
