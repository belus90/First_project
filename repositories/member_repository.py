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