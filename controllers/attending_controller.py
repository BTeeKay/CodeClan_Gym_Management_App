from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attending import Attend

import repositories.attend_repository as attend_repo
import repositories.classes_repository as classes_repo
import repositories.member_repository as member_repo

attending_blueprint = Blueprint("attending", __name__)

@attending_blueprint.route("/attending")
def attending():
    attending = attend_repo.select_all()
    return render_template("attending/index.html", title="Attending", attending=attending)

@attending_blueprint.route("/classes/<id>/attend")
def booking_view(id):
    class1 = classes_repo.select(id)
    attendees = attend_repo.select_class_return_attendees(class1.id)
    members = member_repo.select_all()
    members_ids = []
    attendees_ids = []
    available_members = []
    available_members_ids = []

    for member in members:
        members_ids.append(member.id)
    
    for attendee in attendees:
        attendees_ids.append(attendee.id)
    
    for i in members_ids:
        if i not in attendees_ids:
            available_members_ids.append(i)
    
    for i in available_members_ids:
        member = member_repo.select(i)
        available_members.append(member)

    return render_template("attending/booking.html", title=f"{class1.name} Booking", members=members,
     attendees=attendees,
     class1=class1,
     availablemembers=available_members
     )

@attending_blueprint.route("/classes/<id>/attend", methods=['POST'])
def booking(id):
    member_id = request.form['member_id']
    print(request.form['member_id'])
    member = member_repo.select(member_id)
    class1 = classes_repo.select(id)
    attend1 = Attend(member, class1)
    attend_repo.save(attend1)
    return redirect(f"/classes/{id}/attend")
