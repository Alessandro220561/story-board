#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

from config import app, db
from models import User, Book

if __name__ == "__main__":

    with app.app_context():

        User.query.delete()
        Book.query.delete()

        u1 = User(username="Alex Shaw", email="alex@gmail.com")
        u2 = User(username="Jonathan Sherry", email="johnsher@yahoo.com")
        db.session.add_all([u1, u2])
        db.session.commit()

        b1 = Book(title="IT", author="Stephen King", genre="Horror", pages=645)
        b2 = Book(title="Malice", author="John Gwynne", genre='Fantasy', pages=50)
        db.session.add_all([b1, b2])
        db.session.commit()