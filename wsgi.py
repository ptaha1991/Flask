from werkzeug.security import generate_password_hash

from blog.app import app
from blog.models.database import db

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=5010,
    )


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User

    admin = User(username="admin", email="admin@admin.ru", password=generate_password_hash("admin"), is_staff=True)
    james = User(username="james", email="james@james.ru", password=generate_password_hash("james"))
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print("done! created users:", admin, james)
