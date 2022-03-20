from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fittnes_class import Fitnes_class
import repositories.fittnes_class_repository as fittnes_repository

fittnes_classes_blueprint = Blueprint("fittness classes", __name__)

@fittnes_classes_blueprint.route("/fittness classes")
def members():
    fittnes_classes = fittnes_repository.select_all()
    return render_template("fittness classes/index.html", fittnes_classes = fittnes_classes)

