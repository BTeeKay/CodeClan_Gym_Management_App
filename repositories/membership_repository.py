from db.run_sql import run_sql
from models.membership import Membership
import repositories.member_repository as member_repo
import repositories.classes_repository as classes_repo

def save(membership):
    sql = "INSERT INTO memberships (level, description) VALUES ( ?, ?) RETURNING id"
    values = [membership.level, membership.description]
    results = run_sql( sql, values )
    membership.id = results[0]['id']
    return membership

def delete_all():
    sql = "DELETE FROM memberships"
    run_sql(sql)

# Ally started talk and confused me here
def select(id):
    membership = None
    sql = "SELECT * FROM memberships WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = Membership(result['level'], result['description'], result['id'])
    return user

# write this function below
def select_all():
    memberships = []

    sql = "SELECT * FROM memberships"
    results = run_sql(sql)
    for row in results:
        class1 = Membership(row['level'], row['description'], row['id'])
        memberships.append(class1)
    return memberships