from pyrogue_engine.actors.actor import *
from pyrogue_engine.actors.actor_utils.displayable import *
from pyglet import font

class MenuItem(Actor):
	def __init__(self,layer,text,x,y):
		super().__init__(layer)
		self.x=x
		self.y=y
		self.text=text
		#replacde this to set function
		self.function_on_click = self.print_self
		self.scene.clickables.append(self)
		self.label = pyglet.text.Label(self.text,
                          font_name='Times New Roman',
                          font_size=36,x=self.x,y=self.y)
		self.width = len(self.text)*self.label.font_size
		self.height = self.label.font_size
		self.unlocked=True
	def set_unlocked(self,unlocked):
		self.unlocked = unlocked

	def set_function(self,function):
		self.function_on_click = function
	def print_self(self):
		print("was clicked")
	# in screen coords
	def is_coord_in_box(self,x,y):
		xcheck_1 = x > self.x 		
		xcheck_2 = x < (self.width + self.x)
		ycheck_1 = y > self.y 		
		ycheck_2 = y < (self.width + self.y)
		if (xcheck_1 and xcheck_2 and ycheck_1 and ycheck_2 and self.unlocked):
			return True
		else:
			return False
	
	def on_click(self):
		self.function_on_click()
	
	def delete_self(self):
		self.scene.clickables.remove(self)
		super().delete_self()
		
	def draw(self):
		self.label.draw()
