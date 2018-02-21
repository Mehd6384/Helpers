import matplotlib.pyplot as plt 
import numpy as np 


# To use this class: Simply initialize with the number of actions you want to monitor 
# Then, call draw whenever you want to update the plot 

class ThinkFast(): 

	def __init__(self, nb_actions):

		self.nb_actions = nb_actions
		self.up = False


	def draw(self, vals): 

		if not self.up: 
			self.up = True
			self.init_plot()

		self.update(vals)

	def init_plot(self): 

		plt.style.use('ggplot')
		plt.ion()

		self.fig, self.ax = plt.subplots()
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
			a.matshow(v)
		self.fig.canvas.update()
		self.fig.canvas.flush_events()