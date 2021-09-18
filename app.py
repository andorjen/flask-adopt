"""Flask app for adopt app."""

from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

DEFAULT_IMG_URL="https://i.pinimg.com/originals/4b/d7/c0/4bd7c02c36f2945deeb024254fcce362.jpg"

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
        photo_url = form.photo_url.data or None
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

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_info(pet_id):
    """show the detailed info about one pet, and show a form for editing the pet"""
    pet =  Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or DEFAULT_IMG_URL  
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Updated information for:  {pet.name}.")
        return redirect("/")
    

    else:
        return render_template("pet_edit_form.html", pet=pet, form=form)