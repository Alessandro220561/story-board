#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response, session, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Book

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

def Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

