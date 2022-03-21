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
def new_class():
    fittnes_classes = fittnes_repository.select_all()
    return render_template("/fittness classes/new.html", fittnes_classes = fittnes_classes)

#create
@fittnes_classes_blueprint.route("/fittness classes", methods = ['POST'])
def create_new_class():
    name = request.form['name']
    fittnes_level = request.form['fittnes_level']
    duration = request.form['duration']
    new_class = Fitnes_class(name, fittnes_level, duration)
    fittnes_repository.save(new_class)
    return redirect('/fittness classes')

#delete
@fittnes_classes_blueprint.route("/fittness classes/<id>/delete", methods=['POST'])
def delete_class(id):
    fittnes_repository.delete(id)
    return redirect('/fittness classes')
