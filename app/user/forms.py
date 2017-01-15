from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class RegisterForm(Form):
    name = StringField(
        'name',
        validators=[DataRequired(), Length(min=1, max=100)]
    )
    phone_number = StringField(
        'phone_number',
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    zip_code = StringField(
        'zip_code',
        validators=[DataRequired(), Length(min=5, max=5)]
    )
