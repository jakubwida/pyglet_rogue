from pyrogue_engine.actors.actor import Actor
from pymunk import Vec2d
import math, sys, random
from pyglet.window import key
import pymunk

class PhysicsActor(Actor):

	def __init__(self):
		super().__init__()
		self.mass = 0.3
		self.radius = 25
		self.inertia = pymunk.moment_for_circle(self.mass/5, 0, self.radius, (0,0))
		self.pymunk_body = pymunk.Body(self.mass, self.inertia)
		self.pymunk_body.damping=0.001
		self.pymunk_body.friction=0.95
		
		self.pymunk_body.position = self.x, self.y
		self.pymunk_shape= pymunk.Circle(self.pymunk_body, self.radius, (0,0))
		self.pymunk_shape.elasticity = 0.95

	def set_scene(self,scene):
		super().set_scene(scene)
		self.scene.space.add(self.pymunk_body, self.pymunk_shape)
		self.keys = self.scene.game.keys
		print("phys actor scene set")

	def update(self,dt):
		print(self.keys)
		if self.keys[key.UP]:
			self.pymunk_body.apply_force_at_local_point(Vec2d((0.0,1000.0)),(0.0,0.0))
			
		if self.keys[key.DOWN]:
			self.pymunk_body.apply_force_at_local_point(Vec2d((0.0,-1000.0)),(0.0,0.0))
		if self.keys[key.LEFT]:
			self.pymunk_body.apply_force_at_local_point(Vec2d((-1000.0,0.0)),(0.0,0.0))
		if self.keys[key.RIGHT]:
			self.pymunk_body.apply_force_at_local_point(Vec2d((1000.0,0.0)),(0.0,0.0))
		self.x= self.pymunk_body.position[0]
		self.y= self.pymunk_body.position[1]
