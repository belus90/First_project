import pdb
from models.fittnes_class import Fitnes_class
from models.member import Member
from models.gym import Gym

import repositories.fittnes_class_repository as fittnes_class_repository
import repositories.member_repository as member_repository
import repositories.gym_repository as gym_repository

fittness_class1 = Fitnes_class('Spining', 'Entry','30 min')
fittnes_class_repository.save(fittness_class1)




pdb.set_trace()
