"""Seed file to make sample data for adopt db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

pet = Pet(
    name='Catdog',
    species="dog",
    photo_url="https://www.thesprucepets.com/thmb/wpN_ZunUaRQAc_WRdAQRxeTbyoc=/4231x2820/filters:fill(auto,1)/adorable-white-pomeranian-puppy-spitz-921029690-5c8be25d46e0fb000172effe.jpg",
    age="baby",
    available=True)

pet2 = Pet(
    name='Faloola',
    species="dog",
    photo_url="https://www.rd.com/wp-content/uploads/2019/01/shutterstock_673465372.jpg?fit=700,467",
    age="young",
    available=None)

pet3 = Pet(
    name='Tacos',
    species="porcupine",
    photo_url="https://i.natgeofe.com/n/d0c2bc16-95be-4d1f-a1e4-322a0669a7f2/porcupines_thumb.JPG",
    age="senior",
    available=False)


db.session.add_all([pet, pet2, pet3])
db.session.commit()
