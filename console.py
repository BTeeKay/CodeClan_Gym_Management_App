import pdb

from models.member import Member
from models.membership import Membership
from models.attending import Attend
from models.classes import Classes

import repositories.member_repository as member_repo
import repositories.membership_repository as membership_repo
import repositories.attend_repository as attending_repo
import repositories.classes_repository as classes_repo

attending_repo.delete_all()
member_repo.delete_all()
membership_repo.delete_all()
classes_repo.delete_all()

membership1 = Membership("Platinum", "Is there going to be better than this?")
membership1 = membership_repo.save(membership1)
membership2 = Membership("Gold", "Not as good as Platinum")
membership2 = membership_repo.save(membership2)

member1 = Member("Bob", "Kerr", membership1)
member1 = member_repo.save(member1)
member2 = Member("Tina", "Kerr", membership1)
member2 = member_repo.save(member2)

class1 = Classes("Body Pump", 15, "2022-05-27 15:20")
class1 = classes_repo.save(class1)

attending1 = Attend(member1, class1)
attending1 = attending_repo.save(attending1)

all_members = member_repo.select_all()
all_classes = classes_repo.select_all()
all_attending = attending_repo.select_all()
all_membership = membership_repo.select_all()

pdb.set_trace()