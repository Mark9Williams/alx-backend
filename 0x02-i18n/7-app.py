#!/usr/bin/env python3
""" Mocking a user login system """

from typing import Optional, Dict
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

app: Flask = Flask(__name__)

# initialize Babel for i18n
babel: Babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """App configuration for available languages and defaults."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Select a language translation to use for a request"""
    # 1. Check URL parameter
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    # 2. Check user's preferred locale
    user = g.get("user")
    if user:
        user_locale = user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    # 3. Check request header preferences
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """Determine the best timezone for the user."""
    # 1. Check URL parameter for timezone
    tz = request.args.get("timezone")
    if tz:
        try:
            return pytz.timezone(tz).zone
        except UnknownTimeZoneError:
            pass

    # 2. Check user’s preferred timezone if logged in
    user = g.get("user")
    if user:
        user_timezone = user.get("timezone")
        try:
            return pytz.timezone(user_timezone).zone
        except (UnknownTimeZoneError, TypeError):
            pass

    # 3. Default to UTC
    return "UTC"


def get_user() -> Optional[dict]:
    """ Mock a user login """
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id) if user_id in users else None


@app.before_request
def before_request() -> None:
    """ Find a user if any """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """ Returns the index page """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
