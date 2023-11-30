#!/usr/bin/python3
""" Routes to / """
from flask import Flask

APP = Flask(__name__)


@APP.route('/', strict_slashes=False)
def hello():
    """ A route to / """
    return 'Hello HBNB!'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)
