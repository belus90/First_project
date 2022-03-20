from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
import repositories.gym_repository as gym_repository

gyms_blueprint = Blueprint("gyms", __name__)

@gyms_blueprint.route("/gyms")
def gyms():
    gyms = gym_repository.select_all()
    return render_template("gyms/index.html", gyms = gyms)

@gyms_blueprint.route("/gyms/<id>")
def show(id):
    gym = gym_repository.select(id)
    return render_template("gyms/show.html", gym = gym)

