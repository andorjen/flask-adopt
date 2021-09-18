"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL="https://i.pinimg.com/originals/4b/d7/c0/4bd7c02c36f2945deeb024254fcce362.jpg"

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.String(50),
        nullable=False)

    species = db.Column(
        db.String(50),
        nullable=False)

    photo_url = db.Column(
        db.String,
        default=DEFAULT_IMG_URL,
        nullable=False)

    age = db.Column(
        db.String,
        nullable=False)

    notes = db.Column(
        db.Text)

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True)
