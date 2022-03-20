import pdb
from models.fittnes_class import Fitnes_class
from models.member import Member
from models.gym import Gym

import repositories.fittnes_class_repository as fittnes_class_repository
import repositories.member_repository as member_repository
import repositories.gym_repository as gym_repository

fittnes_class_repository.delete_all()
member_repository.delete_all()
gym_repository.delete_all()

fittness_class1 = Fitnes_class('Spining', 'Entry','30 min')
fittnes_class_repository.save(fittness_class1)


fittness_class2 = Fitnes_class('Pump', 'Medium','45min')
fittnes_class_repository.save(fittness_class2)

fittness_class3 = Fitnes_class('Absolute Abs', 'Hard','25min')
fittnes_class_repository.save(fittness_class3)

member1 = Member('Claire', 'Toth', '09/23/1976','claire@gmail.com')
member_repository.save(member1)


member2 = Member('Sarah', 'Willams', '14/04/2000','sarah.45@hotmail.com')
member_repository.save(member2)


member3 = Member('Balint', 'Szabo', '08/12/1995','balint@gmail.com')
member_repository.save(member3)

gym1 = Gym(member1, fittness_class2)
gym_repository.save(gym1)

gym2 = Gym(member2, fittness_class1)
gym_repository.save(gym2)

gym3 = Gym(member3, fittness_class3)
gym_repository.save(gym3)

gym4 = Gym(member1, fittness_class3)
gym_repository.save(gym4)

pdb.set_trace()
