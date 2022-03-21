from db.run_sql import run_sql
from models.fittnes_class import Fitnes_class
from models.member import Member
from models.gym import Gym

def save(fittnes_class):
    sql = "INSERT INTO fittnes_classes(name, fittnes_level, duration) VALUES ( %s, %s, %s ) RETURNING id"
    values = [fittnes_class.name, fittnes_class.fittnes_level, fittnes_class.duration]
    results = run_sql( sql, values )
    fittnes_class.id = results[0]['id']
    return fittnes_class

def select_all():
    fittnes_classes = []

    sql = "SELECT * FROM fittnes_classes"
    results = run_sql(sql)

    for row in results:
        fittnes_class = Fitnes_class(row['name'], row['fittnes_level'], row['duration'], row['id'])
        fittnes_classes.append(fittnes_class)
    return fittnes_classes

def select(id):
    fittnes_class = None
    sql = "SELECT * FROM fittnes_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        fittnes_class = Fitnes_class(result['name'], result['fittnes_level'], result['duration'], result['id'] )
    return fittnes_class

def delete_all():
    sql = "DELETE FROM fittnes_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fittnes_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def members(fittnes_class):
    members = []
    sql ="SELECT * FROM members  INNER JOIN gyms ON gyms.member_id = members.id WHERE gyms.fittnes_class_id = %s"
    values = [fittnes_class.id]
    result = run_sql(sql, values)

    for row in result:
        member = Member(row['first_name'], row['last_name'], row['date_of_birth'], row['email_address'], row['id'])
        members.append(member)
    return members
    
def update(fittnes_class):
    sql = "UPDATE fittnes_classes SET (name, fittnes_level, duration) = (%s, %s, %s) WHERE id = %s"
    values = [fittnes_class.name, fittnes_class.fittnes_level, fittnes_class.duration, fittnes_class.id]
    print(values)
    run_sql(sql, values)
