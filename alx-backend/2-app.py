#!/usr/bin/env python3
'''adding a get local'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    '''instanciating flask app'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''the get local in quetion'''
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    '''apt apt uh uhhh uhh'''
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
