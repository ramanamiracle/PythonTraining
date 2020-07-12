# -*- coding: UTF-8 -*-
"""
hello_jinja2: Get start with Jinja2 templates
"""
from flask import Flask, render_template, request
from models import get_data, validate_user, add_user

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('j2_query.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/process', methods=['POST'])
def process():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary

    username = request.form.get('username')
    password = request.form.get('password')

    valid_user = validate_user(username, password)

    if valid_user:
        data = get_data()
        return render_template('j2_response.html', data=data)
    else:
        return 'Please enter correct credentials', 400  # 400 Bad Request


@app.route('/save', methods=['POST'])
def save():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary

    username = request.form.get('username')
    password = request.form.get('password')

    response = add_user(username, password)

    if response:
        return render_template('j2_query.html')
    else:
        return 'Unable to signup', 400  # 400 Bad Request


if __name__ == '__main__':
    app.run(debug=True)