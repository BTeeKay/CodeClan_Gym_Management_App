from db.run_sql import run_sql

def save(member):
    sql = "INSERT INTO members (first_name, last_name, membership_id) VALUES ( ?, ?, ? ) RETURNING id"
    values = [member.first_name, member.last_name, member.membership.id]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)