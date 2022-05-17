from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms import validators


class SportgruppeForm(FlaskForm):
    Sportgruppen_ID = StringField("Sportgruppen_ID")
    Gruppenname = TextAreaField("Gruppenname", [validators.InputRequired()])
    Gruendungsdatum = DateField(
        "Gruendungsdatum", [validators.InputRequired()])
    Maskotchen = StringField("Maskotchen", [validators.InputRequired()])
