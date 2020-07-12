# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, request, render_template, redirect, url_for
from pprint import pprint
app = Flask(__name__)


@app.route('/html')
def html():
    """Return an HTML-formatted string and an optional response status code"""
    return render_template('hello.html')


@app.route('/hello')
def hello():
    d = ''
    for key, value in request.args.items():
        d = d + '{}, {}\n'.format(key, value)
    return d


@app.route('/hello/<string:username>')  # URL with a variable
def hello_username(username):    # The function shall take the URL variable as parameter
    return 'Hello, {}'.format(username)


@app.route('/hello/<int:userid>')  # Variable with type filter. Accept only int
def hello_userid(userid):          # The function shall take the URL variable as parameter
    return 'Hello, your ID is: {:d}'.format(userid)


@app.route('/')
def main():
    return redirect(url_for('hello', username='Peter', age=32))


if __name__ == '__main__':
    app.run()