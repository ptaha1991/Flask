from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.models import Article

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
@login_required
def articles_details(article_id: int):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound(f"User #{article_id} doesn't exist!")
    return render_template("articles/details.html", article=article)
