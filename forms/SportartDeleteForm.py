from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class SportartDeleteForm(FlaskForm):
    Sportart_ID = StringField("Sportart_ID", [validators.InputRequired()])
