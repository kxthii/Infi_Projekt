from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class SportgruppeDeleteForm(FlaskForm):
    Sportgruppen_ID = StringField(
        "Sportgruppen_ID", [validators.InputRequired()])
