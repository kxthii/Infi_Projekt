from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from model.models import Sportgruppe, db
from forms.SportgruppeDeleteForm import SportgruppeDeleteForm
from forms.SportgruppeForm import SportgruppeForm


sportgruppe_blueprint = Blueprint('sportgruppe_blueprint', __name__)


@sportgruppe_blueprint.route("/sportgruppe")
def sportgruppe():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    sportgruppe = session.query(Sportgruppe).order_by(
        Sportgruppe.Sportgruppen_ID).all()
    return render_template("sportgruppe/sportgruppe.html", sportgruppe=sportgruppe)


@sportgruppe_blueprint.route("/sportgruppe/add", methods=["GET", "POST"])
def sportgruppe_add():
    sqlalchemy.orm.scoping.scoped_session = db.session

    add_sportgruppe_form = SportgruppeForm()
    if request.method == 'POST':

        if add_sportgruppe_form.validate_on_submit():
            new_sportgruppe = Sportgruppe()

            new_sportgruppe.Gruppenname = add_sportgruppe_form.Gruppenname.data
            new_sportgruppe.Gruendungsdatum = add_sportgruppe_form.Gruendungsdatum.data
            new_sportgruppe.Maskotchen = add_sportgruppe_form.Maskotchen.data

            db.session.add(new_sportgruppe)
            db.session.commit()

            return redirect("/sportgruppe")
        else:
            raise "Fatal Error"
    else:
        return render_template("sportgruppe/sportgruppe_add.html", form=add_sportgruppe_form)


@sportgruppe_blueprint.route("/sportgruppe/edit", methods=["GET", "POST"])
def sportgruppe_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_sportgruppe_form = SportgruppeForm()
    Sportgruppen_ID = request.args["Sportgruppen_ID"]
    sportgruppe_to_edit = session.query(Sportgruppe).filter(
        Sportgruppe.Sportgruppen_ID == Sportgruppen_ID).first()

    if request.method == "POST":
        if edit_sportgruppe_form.validate_on_submit():
            Sportgruppen_ID = edit_sportgruppe_form.Sportgruppen_ID.data
            sportgruppe_to_edit = db.session.query(Sportgruppe).filter(
                Sportgruppe.Sportgruppen_ID == Sportgruppen_ID).first()

            sportgruppe_to_edit.Gruppenname = edit_sportgruppe_form.Gruppenname.data
            sportgruppe_to_edit.Gruendungsdatum = edit_sportgruppe_form.Gruendungsdatum.data
            sportgruppe_to_edit.Maskotchen = edit_sportgruppe_form.Maskotchen.data

            db.session.commit()
        return redirect("/sportgruppe")
    else:
        edit_sportgruppe_form.Sportgruppen_ID.data = sportgruppe_to_edit.Sportgruppen_ID
        edit_sportgruppe_form.Gruppenname.data = sportgruppe_to_edit.Gruppenname
        edit_sportgruppe_form.Gruendungsdatum.data = sportgruppe_to_edit.Gruendungsdatum
        edit_sportgruppe_form.Maskotchen.data = sportgruppe_to_edit.Maskotchen

        return render_template("sportgruppe/sportgruppe_edit.html", form=edit_sportgruppe_form)


@sportgruppe_blueprint.route("/sportgruppe/delete", methods=["post"])
def deleteSportgruppe():
    delete_item_form_obj = SportgruppeDeleteForm()
    if delete_item_form_obj.validate_on_submit():
        # print("7")

        sportgruppe_code_to_delete = delete_item_form_obj.Sportgruppen_ID.data
        sportgruppe_to_delete = db.session.query(Sportgruppe).filter(
            Sportgruppe.Sportgruppen_ID == sportgruppe_code_to_delete)
        sportgruppe_to_delete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"sportgruppe with id {sportgruppe_code_to_delete} has been deleted")

    return redirect("/sportgruppe")
