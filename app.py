from flask import Flask
from model.models import db
from controllers.index import index_blueprint
from controllers.sportart import sportart_blueprint
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

#Datenbankzugriff konfigurieren
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Sport"

csrf = CSRFProtect(app)

db.init_app(app)

#hier blueprint registrieren
app.register_blueprint(index_blueprint)
app.register_blueprint(sportart_blueprint)

app.run(debug=True)
