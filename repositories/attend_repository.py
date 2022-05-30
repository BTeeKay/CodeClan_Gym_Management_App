from db.run_sql import run_sql
from models.attending import Attend

import repositories.classes_repository as classes_repo
import repositories.member_repository as member_repo

def save(attend):
    sql = "INSERT INTO attending (member_id, class_id) VALUES ( ?, ?) RETURNING id"
    values = [attend.member.id, attend.classes.id]
    results = run_sql(sql, values)
    attend.id = results[0]['id']
    return attend

def delete_all():
    sql = "DELETE FROM attending"
    run_sql(sql)

def select_all():
    attending = []

    sql = "SELECT * FROM attending"
    results = run_sql(sql)
    for row in results:
        member = member_repo.select(row['member_id'])
        class1 = classes_repo.select(row['class_id'])
        attend = Attend(member, class1, row['id'])
        attending.append(attend)
    return attending

def select(id):
    attend = None
    sql = "SELECT * FROM attending WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repo.select(result['member_id'])
        class1 = classes_repo.select(result['class_id'])
        attend = Attend(member, class1, result['id'])
    return member

def select_class_return_attendees(id):
    sql = "SELECT * FROM attending WHERE class_id = ?"
    values = [id]
    attendes = run_sql(sql, values)
    persons = []

    for attende in attendes:
        person = member_repo.select(attende['member_id'])
        persons.append(person)
    
    return persons

