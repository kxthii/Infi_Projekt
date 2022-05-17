from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class SportlerDeleteForm(FlaskForm):
    Sportler_ID = StringField("Sportler_ID", [validators.InputRequired()])
