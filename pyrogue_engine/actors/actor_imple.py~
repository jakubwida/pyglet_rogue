from pyrogue_engine.actors.entity import Entity
from pyrogue_engine.actors.actor_utils.controllers.player_controller import *
from pyrogue_engine.actors.actor_utils.displayables.displayable_sprite import DisplayableSprite
import pyglet

class ActorImple(Entity):
	def __init__(self,layer):
		super().__init__(layer)
		self.controller = PlayerController(self.physics_object)
		#self.image = pyglet.resource.image("testimage.png")
		#self.sprite = pyglet.sprite.Sprite(img=self.image,x=0,y=0)
		self.displayable= DisplayableSprite(self)
	def update(self,dt):
		super().update(dt)
		#self.sprite.x=self.x
		#self.sprite.y=self.y

	def draw(self):
		super().draw()
		#self.sprite.draw()
