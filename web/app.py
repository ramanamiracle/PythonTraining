# -*- coding: UTF-8 -*-
"""
hello_jinja2: Get start with Jinja2 templates
"""
from flask import Flask, render_template, request, make_response, jsonify, redirect, session, url_for, escape, g
from models import get_data, validate_user, add_user
import time
from flask_restful import Api, Resource
from mongo_models import add_user, get_user, get_users, delete_user, put_user

app = Flask(__name__)

api_manager = Api(app)
app.config['SECRET_KEY'] = 'sadfsdfs123213afdsada'


@app.before_request
def before_request():
    g.start_time = time.time()  # Store in g, applicable for this request and this user only


@app.teardown_request
def teardown_request(exception=None):
    time_taken = time.time() - g.start_time   # Retrieve from g
    print(time_taken)


@app.route('/')
def main():
    if 'username' in session:
        return 'You are already logged in as %s' % escape(session['username'])
        # Escape special HTML characters (such as <, >) in echoing to prevent XSS
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        valid_user = validate_user(username, password)

        if valid_user:
            session['username'] = username
            data = get_data()
            return render_template('response.html', data=data)
        else:
            return render_template('login.html', message="Please enter correct credentials")
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # Remove 'username' from the session if it exists
    session.pop('username', None)
    return redirect(url_for('main'))


@app.route('/save', methods=['POST'])
def save():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary

    username = request.form.get('username')
    password = request.form.get('password')

    response = add_user(username, password)

    if response:
        return render_template('login.html')
    else:
        return 'Unable to signup', 400  # 400 Bad Request


class User(Resource):
    def get(self, user_id):
        data = get_user(user_id)
        response = jsonify(list(data))
        response.status_code = 200
        return response

    def delete(self, user_id):
        result = delete_user(user_id)
        if result.deleted_count == 1:
            return 'Success', 204
        else:
            return 'Failed', 400

    def put(self, user_id):
        data = request.get_json()
        result = put_user(user_id, data)

        if result.modified_count == 1:
            response = jsonify({'message': 'put success'})
            response.status_code = 200
            return response
        else:
            response = jsonify({'message': 'put failed'})
            response.status_code = 400
            return response


class Users(Resource):
    def get(self):
        data = get_users()
        response = jsonify(list(data))
        response.status_code = 200
        return response

    def post(self):
        """Request data needed for create"""
        data = request.get_json()
        result = add_user(data)

        response = jsonify({'id': str(result.inserted_id)})
        response.status_code = 201
        return response


api_manager.add_resource(User, '/api/user/<user_id>', endpoint='user')
api_manager.add_resource(Users, '/api/user/', endpoint='users')


if __name__ == '__main__':
    app.run(debug=True)