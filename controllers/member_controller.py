from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    return render_template("members/show.html", member = member)

#new
@members_blueprint.route("/members/new", methods = ['GET'])
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