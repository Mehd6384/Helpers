import numpy as np 
# For curriculum learning 
# To use this class, first generate levels and pass them to the Planner. Start the Planner 
# and have it check performance of the agent regurlary 

#Example at the end of the script
class Level(): 

	def __init__(self, success_min, positions,name = '0'): 

		self.success_min = success_min
		self.positions = positions
		self.name = name

	def create_next_level(self, success_min, additional_pos, name = 'next'): 

		new = Level(success_min, self.positions[:], name)
		for p in additional_pos: 
			new.positions.append(p)
		return new 

class Planner(): 

	def __init__(self, env, planning):

		self.level_list = planning
		# for p in self.level_list: 
		# 	print('{} -- Positions {}\n'.format(p.name, p.positions))

		self.env = env
		self.level = 0 

	def get_architecture(self): 

		for p in self.level_list: 
			print('{} -- Positions {}\n'.format(p.name, p.positions))

	def start(self): 

		print('\n***** Starting curriculum *****\n')
		self.env.setTargetPosition(self.level_list[0].positions)
		# for p in self.level_list[0].positions: 
		# 	print(p)
		# input()

	def adjust_complexity(self, successes): 

		current = self.level_list[self.level]
		if successes > current.success_min: 
			self.level = min(self.level+1, len(self.level_list)-1)
			print('Upgrading -- New level is : ', self.level)
			self.env.setTargetPosition(self.level_list[self.level].positions) 
			# for p in self.level_list[self.level].positions: 
			# 	print(p)

# level_00 = Level(80, [[0.3,0.6], [0.7,0.6]], 'Absolute beginner')
# level_0 = level_00.create_next_level(80, [[0.1,0.6], [0.9,0.6]], 'Beginner')
# level_1 = level_0.create_next_level(80, [[0.1,0.3], [0.9,0.3]], 'Easy')
# level_2 = level_1.create_next_level(80, [[0.1,0.1], [0.9,0.1]], 'Medium')
# level_3 = level_2.create_next_level(100, [[0.5,0.5], [0.3,0.3], [0.6,0.3]],'Hard')

# planning = Planner(env, [level_00, level_0, level_1, level_2, level_3])

# planning.start()
