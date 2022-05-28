from db.run_sql import run_sql
from models.classes import Classes

def save(class1):
    sql = "INSERT INTO classes (name, capacity, time) VALUES ( ?, ?, ? ) RETURNING id"
    values = [class1.name, class1.capacity, class1.time]
    results = run_sql(sql, values)
    class1.id = results[0]['id']
    return class1

def delete_all():
    sql = "DELETE FROM classes"
    run_sql(sql)

def select(id):
    class1 = None
    sql = "SELECT * FROM members WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        class1 = Classes(result['name'], result['cap'], result['time'], result['id'])
    return class1