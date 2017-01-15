from app.models import User
from app.weather import Weather
from flask import Blueprint, flash, redirect, render_template, request, url_for
from twilio import twiml

from .forms import RegisterForm

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route("/", methods=['GET'])
def main():
    form = RegisterForm(request.form)
    return render_template('home.html', form=form)


@users_blueprint.route("/register", methods=['POST'])
def register():
    form = RegisterForm(request.form)
    data = dict(request.form)
    data.pop('csrf_token')
    new_user = User(**data)

    if new_user.save():
        flash('Succefully registered.')
        return redirect(url_for('users.main'))
    else:
        flash("That username and/or email alread exists.")
        return redirect(url_for('users.main'))


@users_blueprint.route("/text", methods=['POST'])
def text():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    print from_number
    user = User.query.filter_by(phone_number=from_number).first()
    print user
    resp = twiml.Response()
    if user is None:
        resp.message("Hello my name is PAL, it is nice to meet you!")
    else:
        weather = Weather(user.zip_code)
        message = weather.proccess_command()
        resp.message(message)
    return str(resp)
