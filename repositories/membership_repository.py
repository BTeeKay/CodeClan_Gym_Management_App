from db.run_sql import run_sql

def save(membership):
    sql = "INSERT INTO memberships (level, description) VALUES ( ?, ?) RETURNING id"
    values = [membership.level, membership.description]
    results = run_sql( sql, values )
    membership.id = results[0]['id']
    return membership

def delete_all():
    sql = "DELETE FROM memberships"
    run_sql(sql)