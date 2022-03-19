from importlib.abc import ResourceLoader
from db.run_sql import run_sql
from models.fittnes_class import Fitnes_class
from models.member import Member
from models.gym import Gym

def save(member):
    sql = "INSERT INTO members(first_name, last_name, date_of_birth, email_address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.date_of_birth, member.email_address]
    result = run_sql(sql, values)
    member.id = result[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'],row['date_of_birth'], row['email_address'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM memberes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['date_of_birth'], result['email_address'], result['id'] )
    return member

