import matplotlib.pyplot as plt 
import numpy as np 

class FastPlotter(): 

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



