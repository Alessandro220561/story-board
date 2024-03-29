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

class Signup(Resource):
    def post(self):
        try:
            data = request.get_json()
            user = User(username=data['username'], email=data['email'])
            user.password_hash = data['password']

            db.session.add(user)
            db.session.commit()

            session['user_id'] = user.id

            return make_response(user.to_dict(), 201)
        except:
            return ('Error in signing up', 422)
        
api.add_resource(Signup, '/signup')

class Login(Resource):
    def post(self):
        try:
            user = User.query.filter_by(username=request.get_json()['username']).first()
            if user.authenticate(request.get_json()['password']):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
        except:
            return ("Incorrect Username or Password", 401)
        
api.add_resource(Login, '/login')

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)
    
api.add_resource(Users, '/users')



if __name__ == '__main__':
    app.run(port=5555, debug=True)

