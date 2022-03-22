from importlib.abc import ResourceLoader
from db.run_sql import run_sql
from models.fittnes_class import Fitnes_class
from models.member import Member
from models.gym import Gym

def save(member):
    sql = "INSERT INTO members(first_name, last_name,  email_address, date_of_birth) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name,  member.email_address, member.date_of_birth]
    result = run_sql(sql, values)
    member.id = result[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email_address'],row['date_of_birth'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['email_address'], result['date_of_birth'], result['id'] )
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (first_name, last_name,  email_address, date_of_birth) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.email_address, member.date_of_birth, member.id]
    print(values)
    run_sql(sql, values)

