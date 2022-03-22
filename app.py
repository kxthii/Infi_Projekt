from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
#from editItemFrom import EditItemForm
from model.models import db, Sport
#from addItemForm import AddItemForm
#from deleteItemForm import DeleteItemForm

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

#Datenbankzugriff konfigurieren
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Sport"
db.init_app(app)
