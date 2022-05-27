import pdb

from models.member import Member
from models.membership import Membership

import repositories.member_repository as member_repo
import repositories.membership_repository as membership_repo

member_repo.delete_all()
membership_repo.delete_all()

membership1 = Membership("Platinum", "Is there going to be better than this?")
membership1 = membership_repo.save(membership1)

member1 = Member("Bob", "Kerr", membership1)
member1 = member_repo.save(member1)

pdb.set_trace()