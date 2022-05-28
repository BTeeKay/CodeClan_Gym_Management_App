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
    sql = "SELECT * FROM classes WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        class1 = Classes(result['name'], result['capacity'], result['time'], result['id'])
    return class1

def select_all():
    classes = []

    sql = "SELECT * FROM classes"
    results = run_sql(sql)
    for row in results:
        class1 = Classes(row['name'], row['capacity'], row['time'], row['id'])
        classes.append(class1)
    return classes