class Layer:
	def __init__(self):
		self.actors =[]
		self.scene = None

	def update(self,dt):
		for actor in self.actors:
			actor.update(dt)

	def draw(self):
		self.actors.sort(key=lambda actor: actor.y, reverse=True)
		for actor in self.actors:
			actor.draw()

	def add_actor(self,actor):
		self.actors.append(actor)
		actor.set_layer(self)
		actor.set_scene(self.scene)


	def remove_actor(self,actor):
		self.actors.remove(actor)

	def set_scene(self,scene):
		self.scene=scene
		for actor in self.actors:
			actor.set_scene(scene)
