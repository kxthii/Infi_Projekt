from tkinter import HIDDEN
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

sportart = Sportart.Sportart
class SportgruppeForm(FlaskForm):
    Sportgruppen_ID = StringField("Sportgruppen_ID")
    Gruppenname = TextAreaField("Gruppenname",[validators.InputRequired()])
    Gruendungsdatum = DateField("Gruendungsdatum", [validators.InputRequired()])
    Maskotchen = StringField("Maskotchen", [validators.InputRequired()])
    
  


    