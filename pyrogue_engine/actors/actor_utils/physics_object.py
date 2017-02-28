import pymunk

class PhysicsObject:
	def __init__(self,actor): 
		self.actor = actor
		self.mass =0.3
		self.radius =25
		self.inertia = pymunk.moment_for_circle(self.mass/5, 0, self.radius, (0,0))
		self.elasticity = 0.95
		self.damping = 0.001
		self.friction =0.95
		self.initialise_physics()

		self.pymunk_body = pymunk.Body(self.mass, self.inertia)
		self.pymunk_body.damping=self.damping
		self.pymunk_body.friction=self.friction
		
		self.pymunk_body.position = actor.x, actor.y
		self.pymunk_shape= pymunk.Circle(self.pymunk_body, self.radius, (0,0))
		self.pymunk_shape.elasticity = self.elasticity
		
		actor.scene.space.add(self.pymunk_body, self.pymunk_shape)	
	
	def initialise_physics(self):pass
		
		
		 
	def update(self,dt): pass

