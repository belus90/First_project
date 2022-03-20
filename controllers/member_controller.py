from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.fittnes_class_repository as fittnes_class_repository
import repositories.gym_repository as gym_repository
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

#new member
@members_blueprint.route("/members/new", methods = ['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", members = members)



