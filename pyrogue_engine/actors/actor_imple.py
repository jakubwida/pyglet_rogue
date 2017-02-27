from pyrogue_engine.actors.physics_actor import PhysicsActor

import pyglet

class ActorImple(PhysicsActor):
	def __init__(self):
		super().__init__()
		self.image = pyglet.resource.image("testimage.png")
		self.sprite = pyglet.sprite.Sprite(img=self.image,x=0,y=0)
	def update(self,dt):
		super().update(dt)
		self.sprite.x=self.x
		self.sprite.y=self.y

	def draw(self):
		self.sprite.draw()
