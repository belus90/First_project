from sys import getfilesystemencodeerrors
from db.run_sql import run_sql
from models.gym import Gym
import repositories.fittnes_class_repository as fittnes_repository
import repositories.member_repository as member_repository

def save(gym):
    sql  = "INSERT INTO gyms(member_id, fittnes_class_id) VALUES (%s, %s) RETURNING id"
    values = [gym.member.id, gym.fittnes_class.id]
    results = run_sql(sql, values)
    gym.id = results[0]['id']
    return gym

def select_all():
    gyms = []

    sql = "SELECT * FROM gyms"
    result = run_sql(sql)

    for row in result:
        member = member_repository.select(row['member_id'])
        fittnes_class = fittnes_repository.select(row['fittnes_select_id'])
        gym = Gym(member, fittnes_class, row['id'])
        gyms.append(gym)
    return gyms 

def select(id):
    sql = "SELECT FROM gyms WHERE id = %s"
    values = [id]
    run_sql(sql, values)

    
def delete_all():
    sql = "DELETE FROM gyms"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gyms WHERE id = %s"
    values = [id]
    run_sql(sql, values)


