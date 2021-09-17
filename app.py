"""Flask app for adopt app."""

from flask import Flask, redirect, render_template, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get('/')
def show_all_pets():
    """render homepage template, show all pets with pictures, names, and availability"""
    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)
