#!/usr/bin/env python3
""" configure babel """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ App configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Locale selector """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'])
def index():
    """ Index route """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
