from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from model.models import Sportart, db
from forms.SportartDeleteForm import SportartDeleteForm
from forms.SportartForm import SportartForm
from random import randint, random

sportart_blueprint = Blueprint('sportart_blueprint', __name__)

@sportart_blueprint.route("/sportart")
def sportart():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    sportart = session.query(Sportart).order_by(Sportart.Sportart_ID).all()
    return render_template("sportart/sportart.html", sportart = sportart)


@sportart_blueprint.route("/sportart/add", methods=["GET","POST"])
def sportart_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    add_sportart_form = SportartForm()
    if request.method == 'POST':
        
        if add_sportart_form.validate_on_submit():
            new_sportart = Sportart()
            
            #new_sportart.Sportart_ID = add_sportart_form.Sportart.data
            new_sportart.Sportart = add_sportart_form.Sportart.data
        
            db.session.add(new_sportart)
            db.session.commit()

            return redirect("/sportart")
        else:
            raise "Fatal Error"
    else:
        return render_template("sportart/sportart_add.html", form=add_sportart_form)



@sportart_blueprint.route("/sportart/edit", methods=["GET","POST"])
def sportart_edit():
    session : sqlalchemy.orm.scoping.scoped_session = db.session

    edit_sportart_form = SportartForm()
    Sportart_ID = request.args["Sportart_ID"]
    sportart_to_edit = session.query(Sportart).filter(Sportart.Sportart_ID == Sportart_ID).first()
    
    if request.method == "POST":
        if edit_sportart_form.validate_on_submit():
            Sportart_ID = edit_sportart_form.Sportart_ID.data
            sportart_to_edit = db.session.query(Sportart).filter(Sportart.Sportart_ID == Sportart_ID).first()
            
            sportart_to_edit.Sportart = edit_sportart_form.Sportart.data
            

            db.session.commit()
        return redirect("/sportart")
    else:
        edit_sportart_form.Sportart_ID.data = sportart_to_edit.Sportart_ID
        edit_sportart_form.Sportart.data = sportart_to_edit.Sportart
        
        return render_template("sportart/sportart_edit.html",form = edit_sportart_form)

@sportart_blueprint.route("/sportart/delete", methods=["post"])
def deleteSportart():
    delete_item_form_obj = SportartDeleteForm()
    if delete_item_form_obj.validate_on_submit():
        #print("7")

        sportart_code_to_delete = delete_item_form_obj.Sportart_ID.data
        sportart_to_delete = db.session.query(Sportart).filter(Sportart.Sportart_ID == sportart_code_to_delete)
        sportart_to_delete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"sportart with id {sportart_code_to_delete} has been deleted")    

    return redirect("/sportart")