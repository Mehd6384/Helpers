import matplotlib.pyplot as plt 
import numpy as np 


# To use this class: Simply initialize with the number of actions you want to monitor 
# Then, call draw whenever you want to update the plot
# It is possible to set up names for the bars: After creating an instance, call instance.set_names(names) 

class ThinkFast(): 

	def __init__(self, nb_actions):

		self.nb_actions = nb_actions
		self.up = False
		self.has_name = False

	def set_names(self, names): 

		self.has_name = True 
		self.names = names

	def draw(self, vals): 

		if not self.up: 
			self.up = True
			self.init_plot()

		self.update(vals)

	def init_plot(self): 

		plt.style.use('ggplot')
		plt.ion()

		self.fig, self.ax = plt.subplots()
		self.ax.set_title('Agents actions probabilities')
		self.ax.set_xlabel('Possible actions')
		self.ax.set_ylabel('Probability')
		if self.has_name: 
			self.ax.set_xticks(np.arange(self.nb_actions)*1. + 0.5)
			self.ax.set_xticklabels(self.names)
		self.ax.set_ylim(0.,1.)

		x = np.arange(self.nb_actions)
		y = np.zeros_like(x)
		self.bars = self.ax.bar(x,y, color = 'grey')
		self.fig.canvas.draw()

	def update(self, vals): 

		for v,b in zip(vals,self.bars): 
			b.set_height(v)
			self.ax.draw_artist(b)

		self.fig.canvas.update()
		self.fig.canvas.flush_events()



class FastStateValue(): # To use this class, initialize with max steps of the environment. Then, draw with the latest state 
						# value and information concerning termination of the episode 
						# Also, using previous allows to see previous state estimations of the critic. Can be useful

	def __init__(self, max_length, previous = 3): 

		self.max_length = max_length + 1
		self.values = np.zeros((self.max_length))
		self.count = 0
		self.up = False
		self.show_old = False
		if previous > 0: 
			self.previous_size = previous
			self.show_old = True
			self.count_old = 0
			self.previous = np.zeros((previous, self.max_length))

	def draw(self,y,done):

		self.values[self.count] = y
		self.count += 1 

		if done: 
			self.count = 0 
			
			if self.show_old: 
				for i in reversed(range(self.previous_size)): 
					if i == 0: 
						self.previous[i,:] = self.values
					else: 
						self.previous[i,:] = self.previous[i-1,:]
				for i in range(self.previous_size): 
					self.old_lines[i].set_ydata(self.previous[i,:])
				# self.previous[self.count_old,:] = self.values
				# self.count_old = (self.count_old+1)%self.previous_size
				# for i in range(self.previous_size): 
				# 	self.old_lines[i].set_ydata(self.previous[i,:])

			self.values *= 0. 

		if not self.up: 
			self.up = True
			self.init_plot()

		self.update(done)

	def init_plot(self): 

		plt.style.use('ggplot')
		plt.ion()

		self.fig, self.ax = plt.subplots()
		self.ax.set_title('States values in current episode')
		self.ax.set_xlabel('Steps in episode')
		self.ax.set_ylabel('State value')
		self.ax.set_xlim(0,self.max_length)

		self.line, = self.ax.plot(np.arange(self.max_length), self.values)

		if self.show_old: 
			self.old_lines = []
			for i in range(self.previous_size): 
				l, = self.ax.plot(np.arange(self.max_length), self.values)
				self.old_lines.append(l)

			legende = ['State values at n-{}'.format(i) for i in range(self.previous_size)]
			legende.insert(0,'Current state values')
			self.ax.legend(legende)

		self.fig.canvas.draw()

	def update(self, done): 

		self.line.set_ydata(self.values)
		self.ax.draw_artist(self.line)
		v_min, v_max = np.min(self.values), np.max(self.values)
		big = np.max([np.abs(v_min), v_max])
		if not done: self.ax.set_ylim(-big*1.1, big*1.1)

		self.fig.canvas.update()
		self.fig.canvas.flush_events()


# To use this class: Simply initialize with the number of matrices you want to monitor 
# This will create axis
# Then, call draw whenever you want to update the plot 

class FastWeight(): 

	def __init__(self, nb): 

		self.nb = nb
		self.up = False
		self.images = []

	def draw(self, vals): 

		if not self.up: 
			self.up = True
			self.init_plot()

		self.update(vals)

	def init_plot(self): 

		plt.style.use('ggplot')
		plt.ion()

		self.fig, self.ax = plt.subplots(1,self.nb)
		x = np.zeros((10,10))
		for a in self.ax: 
			im = a.matshow(x)
			self.images.append(im)

		self.fig.canvas.draw()

	def update(self, vals): 

		for i,a,v in zip(self.images, self.ax, vals): 
			i = a.matshow(v)

		self.fig.canvas.update()
		self.fig.canvas.flush_events()