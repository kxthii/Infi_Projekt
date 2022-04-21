from tkinter import HIDDEN
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

class SportartForm(FlaskForm):
    Sportart_ID = StringField("Sportart_ID")
    Sportart = StringField("Sportart",[validators.InputRequired()])
    
    