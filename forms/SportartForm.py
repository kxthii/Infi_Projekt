from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class SportartForm(FlaskForm):
    Sportart_ID = StringField("Sportart_ID")
    Sportart = StringField("Sportart", [validators.InputRequired()])
