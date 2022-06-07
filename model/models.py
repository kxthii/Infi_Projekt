# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Sportart(db.Model):
    __tablename__ = 'sportart'

    Sportart_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Sportart = db.Column(db.String(60))


class Sportgruppe(db.Model):
    __tablename__ = 'sportgruppe'

    Sportgruppen_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Gruppenname = db.Column(db.String(64))
    Gruendungsdatum = db.Column(db.Date)
    Maskotchen = db.Column(db.String(64))
    Sportart_ID = db.Column(db.ForeignKey('sportart.Sportart_ID'), index=True)

    sportart = db.relationship(
        'Sportart', primaryjoin='Sportgruppe.Sportart_ID == Sportart.Sportart_ID', backref='sportgruppes')


class SportgruppeSportler(db.Model):
    __tablename__ = 'sportgruppe_sportler'

    Sportgruppe_Sportler_ID = db.Column(
        db.Integer, primary_key=True, unique=True)
    Sportler_ID = db.Column(db.ForeignKey('sportler.Sportler_ID'), index=True)
    Sportgruppen_ID = db.Column(db.ForeignKey(
        'sportgruppe.Sportgruppen_ID'), index=True)

    sportgruppe = db.relationship(
        'Sportgruppe', primaryjoin='SportgruppeSportler.Sportgruppen_ID == Sportgruppe.Sportgruppen_ID', backref='sportgruppe_sportlers')
    sportler = db.relationship(
        'Sportler', primaryjoin='SportgruppeSportler.Sportler_ID == Sportler.Sportler_ID', backref='sportgruppe_sportlers')


class Sportler(db.Model):
    __tablename__ = 'sportler'

    Sportler_ID = db.Column(db.Integer, primary_key=True, unique=True)
    Geburtsdatum = db.Column(db.Date)
    Vorname = db.Column(db.String(64))
    Nachname = db.Column(db.String(64))
    Größe = db.Column(db.String(64))
