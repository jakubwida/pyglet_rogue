import pyglet
import pymunk

class Scene:
	def __init__(self):
		self.layers=[]
		self.game = None
		self.space = pymunk.Space()
		self.space.damping=0.001
		self.space.gravity = (0.0, 0.0)

	def set_game(self,game):
		self.game = game

	def add_layer(self,layer):
		self.layers.append(layer)
		layer.set_scene(self)

	
	def draw(self):
		for layer in self.layers:
			layer.draw()

	def update(self,dt):
		for layer in self.layers:
			layer.update(dt)
		self.space.step(dt)
		



