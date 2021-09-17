"""Flask app for adopt app."""

from flask import Flask, redirect, render_template, request, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get("/")
def show_all_pets():
    """render homepage template, show all pets with pictures, names, and availability"""
    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, 
                        age=age, notes=notes, available=True)
        
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added new pet:  {name}.")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)