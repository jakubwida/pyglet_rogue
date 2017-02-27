class Actor:
	def __init__(self):
		self.layer= None
		self.scene= None
		self.y=0
		self.x=0
	
	def set_layer(self,layer):
		self.layer= layer

	def set_scene(self,scene):
		self.scene = scene 
		print("phys actor scene set")
	
	def delete_self(self):
		self.layer.remove_actor(self)

	def update(self,dt): pass
	
	def draw(self): pass
		
