from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from model.models import Sportler, db
from forms.SportlerDeleteForm import SportlerDeleteForm
from forms.SportlerForm import SportlerForm

sportler_blueprint = Blueprint('sportler_blueprint', __name__)


@sportler_blueprint.route("/sportler")
def sportler():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sportler = session.query(Sportler).order_by(Sportler.Sportler_ID).all()
    return render_template("sportler/sportler.html", sportler=sportler)


@sportler_blueprint.route("/sportler/add", methods=["GET", "POST"])
def sportler_add():
    sqlalchemy.orm.scoping.scoped_session = db.session

    add_sportler_form = SportlerForm()
    if request.method == 'POST':

        if add_sportler_form.validate_on_submit():
            new_sportler = Sportler()

            new_sportler.Geburtsdatum = add_sportler_form.Geburtsdatum.data
            new_sportler.Vorname = add_sportler_form.Vorname.data
            new_sportler.Nachname = add_sportler_form.Nachname.data
            new_sportler.Größe = add_sportler_form.Größe.data

            db.session.add(new_sportler)
            db.session.commit()

            return redirect("/sportler")
        else:
            raise "Fatal Error"
    else:
        return render_template("sportler/sportler_add.html", form=add_sportler_form)


@sportler_blueprint.route("/sportler/edit", methods=["GET", "POST"])
def sportler_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_sportler_form = SportlerForm()
    Sportler_ID = request.args["Sportler_ID"]
    sportler_to_edit = session.query(Sportler).filter(
        Sportler.Sportler_ID == Sportler_ID).first()

    if request.method == "POST":
        if edit_sportler_form.validate_on_submit():
            Sportler_ID = edit_sportler_form.Sportler_ID.data
            sportler_to_edit = db.session.query(Sportler).filter(
                Sportler.Sportler_ID == Sportler_ID).first()

            sportler_to_edit.Geburtsdatum = edit_sportler_form.Geburtsdatum.data
            sportler_to_edit.Vorname = edit_sportler_form.Vorname.data
            sportler_to_edit.Nachname = edit_sportler_form.Nachname.data
            sportler_to_edit.Größe = edit_sportler_form.Größe.data

            db.session.commit()
        return redirect("/sportler")
    else:
        edit_sportler_form.Sportler_ID.data = sportler_to_edit.Sportler_ID
        edit_sportler_form.Geburtsdatum.data = sportler_to_edit.Geburtsdatum
        edit_sportler_form.Vorname.data = sportler_to_edit.Vorname
        edit_sportler_form.Nachname.data = sportler_to_edit.Nachname
        edit_sportler_form.Größe.data = sportler_to_edit.Größe

        return render_template("sportler/sportler_edit.html", form=edit_sportler_form)


@sportler_blueprint.route("/sportler/delete", methods=["post"])
def deleteSportler():
    delete_item_form_obj = SportlerDeleteForm()
    if delete_item_form_obj.validate_on_submit():
        # print("7")

        sportler_code_to_delete = delete_item_form_obj.Sportler_ID.data
        sportler_to_delete = db.session.query(Sportler).filter(
            Sportler.Sportler_ID == sportler_code_to_delete)
        sportler_to_delete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"sportler with id {sportler_code_to_delete} has been deleted")

    return redirect("/sportler")
