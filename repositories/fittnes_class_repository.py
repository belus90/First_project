from db.run_sql import run_sql
from models.fittnes_class import Fitnes_class
from models.member import Member

def save(fittnes_class):
    sql = "INSERT INTO fittnes_classes(name, fittnes_level, duration) VALUES ( %s, %s, %s ) RETURNING id"
    values = [fittnes_class.name, fittnes_class.fittnes_level, fittnes_class.duration]
    results = run_sql( sql, values )
    fittnes_class.id = results[0]['id']
    return fittnes_class

def select_all():
    fittnes_classes = []

    sql = "SELECT * FROM fittness_classes"
    results = run_sql(sql)

    for row in results:
        fittnes_class = Fitnes_class(row['name'], row['fittnes_level'], row['duration'], row['id'])
        fittnes_classes.append(fittnes_class)
    return fittnes_classes
