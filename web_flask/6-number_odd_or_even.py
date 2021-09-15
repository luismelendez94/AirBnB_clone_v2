#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    """ Display a message """
    return "Hello HBNB!"


@app.route('/hbnb')
def holby():
    """ Display a message """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """ Display message followed by <text> """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Display message followed by <text> """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def is_number(n):
    """ Display message if n is integer """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_temp(n):
    """ Display HTML if n is integer """
    if isinstance(n, int):
        return render_template('/5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def num_odd_even(n):
    """ Display HTML if n is integer """
    odd_even = ''
    if isinstance(n, int):
        if (n % 2) == 0:
            odd_even = 'even'
        else:
            odd_even = 'odd'
        return render_template('/6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
