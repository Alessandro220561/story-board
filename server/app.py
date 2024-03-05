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

class Auth(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            return make_response(user.to_dict(), 200)
        except:
            return('Unauthorized', 401)

api.add_resource(Auth, '/auth')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

