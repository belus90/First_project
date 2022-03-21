import email
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fittnes_class import Fitnes_class
import repositories.fittnes_class_repository as fittnes_repository

fittnes_classes_blueprint = Blueprint("fittness classes", __name__)

@fittnes_classes_blueprint.route("/fittness classes")
def members():
    fittnes_classes = fittnes_repository.select_all()
    return render_template("fittness classes/index.html", fittnes_classes = fittnes_classes)

@fittnes_classes_blueprint.route("/fittness classes/<id>")
def show(id):
    fittnes_class = fittnes_repository.select(id)
    members = fittnes_repository.members(fittnes_class)
    return render_template("fittness classes/show.html", fittnes_class = fittnes_class, members = members)

#new
@fittnes_classes_blueprint.route("/fittness classes/new", methods = ['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("/members/new.html", members = members)
#create
@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email_address = request.form['email_address']
    date_of_birth = request.form['date_of_birth']
    member = Member(first_name, last_name, email_address, date_of_birth)
    member_repository.save(member)
    return redirect('/members')
