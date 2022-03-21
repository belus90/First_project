from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fittnes_class import Fitnes_class
from models.gym import Gym
import repositories.gym_repository as gym_repository
import repositories.fittnes_class_repository as fittnes_class_repository
import repositories.member_repository as member_repository

gyms_blueprint = Blueprint("gyms", __name__)


@gyms_blueprint.route("/gyms")
def gyms():
    gyms = gym_repository.select_all() 
    return render_template("gyms/index.html", gyms = gyms)


@gyms_blueprint.route("/gyms/<id>/delete", methods=['POST'])
def delete_member(id):
    gym_repository.delete(id)
    return redirect('/gym')
