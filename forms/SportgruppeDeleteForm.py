from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

class SportgruppeDeleteForm(FlaskForm):
    Sportgruppen_ID = StringField("Sportgruppen_ID",[validators.InputRequired()])