from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    serialize_rules = ('-reading_logs.user', )

    reading_logs = db.relationship("ReadingLog", back_populates="user")

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    pages = db.Column(db.Integer)

    serialize_rules = ('-reading_logs.book', )

    reading_logs = db.relationship("ReadingLog", back_populates="book")

class ReadingLog(db.Model, SerializerMixin):
    __tablename__ = 'reading_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    serialize_rules = ('-user.reading_logs', '-book.reading_logs')

    user = db.relationship("User", back_populates="reading_logs")
    book = db.relationship("Book", back_populates="reading_logs")

# class UserLog(db.Model, SerializerMixin):
#     __tablename__ = 'user_logs'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     reading_log_id = db.Column(db.Integer, db.ForeignKey('reading_logs.id'))
#     favorite = db.Column(db.Boolean)