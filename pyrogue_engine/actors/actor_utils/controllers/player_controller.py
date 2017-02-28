from pyrogue_engine.actors.actor_utils.controller import *
from pyglet.window import key
from pymunk import Vec2d

class PlayerController(Controller):
	def __init__(self,physics_object):
		super().__init__(physics_object)
		self.keys = physics_object.actor.scene.game.keys

	def update(self,dt):
		super().update(dt)
		if self.keys[key.UP]:
			self.physics_object.pymunk_body.apply_force_at_local_point(Vec2d((0.0,1000.0)),(0.0,0.0))
			
		if self.keys[key.DOWN]:
			self.physics_object.pymunk_body.apply_force_at_local_point(Vec2d((0.0,-1000.0)),(0.0,0.0))
		if self.keys[key.LEFT]:
			self.physics_object.pymunk_body.apply_force_at_local_point(Vec2d((-1000.0,0.0)),(0.0,0.0))
		if self.keys[key.RIGHT]:
			self.physics_object.pymunk_body.apply_force_at_local_point(Vec2d((1000.0,0.0)),(0.0,0.0))
		self.physics_object.actor.x= self.physics_object.pymunk_body.position[0]
		self.physics_object.actor.y= self.physics_object.pymunk_body.position[1]
