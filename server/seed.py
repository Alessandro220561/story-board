#!/usr/bin/env python3

from config import app, db
from models import User, Book, ReadingLog
from datetime import datetime

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

        rl1 = ReadingLog(user_id=1, book_id=1, start_date=datetime(2024, 1, 27), end_date=datetime(2024, 2, 27))
        rl2 = ReadingLog(user_id=2, book_id=2, start_date=datetime(2024, 1, 3), end_date=datetime(2024, 2, 7))
        db.session.add_all([rl1, rl2])
        db.session.commit()