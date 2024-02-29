#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Book, ReadingLog

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)
    
class Books(Resource):
    def get(self):
        books = [book.to_dict() for book in Book.query.all()]
        return make_response(jsonify(books), 200)
    
class ReadingLogs(Resource):
    def get(self):
        reading_logs = [logs.to_dict() for logs in ReadingLog.query.all()]
        return make_response(jsonify(reading_logs), 200)
    
api.add_resource(Users, '/users')
api.add_resource(Books, "/books")
api.add_resource(ReadingLogs, "/reading_logs")


if __name__ == '__main__':
    app.run(port=5555, debug=True)

