class Layer:
	def __init__(self,scene):
		self.actors =[]
		self.scene = scene
		self.scene.add_layer(self)

	def update(self,dt):
		for actor in self.actors:
			actor.update(dt)

	def draw(self):
		self.actors.sort(key=lambda actor: actor.y, reverse=True)
		for actor in self.actors:
			actor.draw()

	def add_actor(self,actor):
		self.actors.append(actor)


	def remove_actor(self,actor):
		self.actors.remove(actor)


