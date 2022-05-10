from tkinter import HIDDEN
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators


class SportlerForm(FlaskForm):
    Sportler_ID = StringField("Sportler_ID")
    Geburtsdatum = DateField("Geburtsdatum",[validators.InputRequired()])
    Vorname = StringField("Vorname", [validators.InputRequired()])
    Nachname = StringField("Nachname", [validators.InputRequired()])
    Größe = StringField("Größe", [validators.InputRequired()])