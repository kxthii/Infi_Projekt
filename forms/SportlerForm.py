from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms import validators


class SportlerForm(FlaskForm):
    Sportler_ID = StringField("Sportler_ID")
    Geburtsdatum = DateField("Geburtsdatum", [validators.InputRequired()])
    Vorname = StringField("Vorname", [validators.InputRequired()])
    Nachname = StringField("Nachname", [validators.InputRequired()])
    Größe = StringField("Größe", [validators.InputRequired()])
