from flask import Flask, render_template
from flask_migrate import Migrate

from blog.models.database import db
from blog.views.articles import articles_app
from blog.views.auth import auth_app, login_manager
from blog.views.authors import authors_app
from blog.views.tags import tags_app
from blog.views.users import users_app

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")
app.register_blueprint(tags_app, url_prefix="/tags")

# cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.BaseConfig")
login_manager.init_app(app)
db.init_app(app)

migrate = Migrate(app, db, compare_type=True, render_as_batch=True)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag

    tags = ("flask", "django", "python", "gb", "sqlite")
    for item in tags:
        db.session.add(Tag(name=item))
    db.session.commit()
    print("created tags")
