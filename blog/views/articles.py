from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles_app = Blueprint("articles_app", __name__)

ARTICLES = {
    1: {
        "title": "Test1",
        "text": "Lorem ipsum tellus metus commodo bibendum, justo diam sem eros nec sed orci ligula in morbi sed magna metus cursus, nibh curabitur nulla donec mauris. In commodo integer morbi, a diam enim, leo eros orci amet tempus fusce curabitur in nulla sapien, quisque, sodales: mauris.",
        "author": 1,
    },
    2: {
        "title": "Test2",
        "text": "At malesuada: leo cursus eu, molestie magna vivamus arcu ipsum mattis metus malesuada bibendum leo sagittis ipsum ligula, congue adipiscing vitae commodo. Magna ultricies maecenas eros arcu pellentesque eros integer a metus et congue sem sit — proin at arcu. Donec malesuada leo lorem in tempus eu pharetra pellentesque justo ligula porttitor in ornare, ut enim vivamus cursus commodo gravida nam.",
        "author": 3,
    },
    3: {
        "title": "Test3",
        "text": "Gravida bibendum, amet maecenas leo porttitor bibendum mattis mauris congue, leo mauris enim risus cursus orci, molestie leo, non. In, pharetra sagittis sit porta, nulla in eros diam integer. Quisque morbi porttitor sodales quisque magna proin diam proin, leo ligula vulputate risus proin, justo auctor, integer tellus lectus enim maecenas justo. Commodo eu et, adipiscing porta porttitor duis at auctor bibendum. Quisque bibendum tempus urna non a morbi, enim tellus, commodo porta odio et cursus vulputate ultricies mauris: nec. Morbi sodales, eget nibh orci cursus adipiscing lorem ornare, congue metus molestie, malesuada elementum.",
        "author": 2,
    },
}


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def articles_details(article_id: int):
    try:
        article_title = ARTICLES[article_id]["title"]
        article_text = ARTICLES[article_id]["text"]
        article_author = ARTICLES[article_id]["author"]
    except KeyError:
        raise NotFound(f"User #{article_id} doesn't exist!")
    return render_template(
        "articles/details.html",
        article_id=article_id,
        article_title=article_title,
        article_text=article_text,
        article_author=article_author,
    )
