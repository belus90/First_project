import pdb
from models.fittnes_class import Fitnes_class
from models.member import Member
from models.gym import Gym

import repositories.fittnes_class_repository as fittnes_class_repository
import repositories.member_repository as member_repository
import repositories.gym_repository as gym_repository

# fittnes_class_repository.delete_all()
# member_repository.delete_all()
# gym_repository.delete_all()

fittness_class1 = Fitnes_class('Spining', 'Entry','30 min')
fittnes_class_repository.save(fittness_class1)


fittness_class2 = Fitnes_class('Pump', 'Medium','45min')
fittnes_class_repository.save(fittness_class2)

fittness_class3 = Fitnes_class('Absolute Abs', 'Hard','25min')
fittnes_class_repository.save(fittness_class3)



pdb.set_trace()
