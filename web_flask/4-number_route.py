#!/usr/bin/python3
"""
Start a Flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Display a message """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def holby():
    """ Display a message """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Display message followed by <text> """
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """ Display message followed by <text> """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """ Display message if n is integer """
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
