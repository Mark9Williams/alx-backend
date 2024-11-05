#!/usr/bin/env python3
""" Babel Flask extension """
from flask import Flask, render_template
from flask_babel import Babel
from typing import List

app: Flask = Flask(__name__)


class Config:
    """Configuration class for Flask and Babel settings"""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """Returns the index page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
