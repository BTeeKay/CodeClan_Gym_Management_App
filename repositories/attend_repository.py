from db.run_sql import run_sql

def save(attend):
    sql = "INSERT INTO attending (member_id, class_id) VALUES ( ?, ?) RETURNING id"
    values = [attend.member.id, attend.classes.id]
    results = run_sql(sql, values)
    attend.id = results[0]['id']
    return attend

def delete_all():
    sql = "DELETE FROM attending"
    run_sql(sql)