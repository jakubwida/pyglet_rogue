import pyglet
import pymunk
from pyrogue_engine.utils.scene import Scene

class GameScene(Scene):
	def __init__(self,game):
		super().__init__(game)
		self.space = pymunk.Space()
		self.space.damping=0.001
		self.space.gravity = (0.0, 0.0)

	def update(self,dt):
		super().update(dt)
		self.space.step(dt)
		




