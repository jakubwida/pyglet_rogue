import pyglet 
from pyglet.window import key
from pyglet.gl import *

from pyglet.window import mouse

class Game:
	def __init__(self):
		self.win_scale=2.0
		self.game_window = pyglet.window.Window(800, 600,vsync=False) 
		pyglet.clock.set_fps_limit(60)
		self.fps_display = pyglet.clock.ClockDisplay(format='%(fps).2f fps')
		self.game_window.on_draw = self.on_draw
		self.game_window.on_mouse_press = self.on_mouse_press
		glScalef(self.win_scale, self.win_scale, self.win_scale)

		self.keys = key.KeyStateHandler()
		self.game_window.push_handlers(self.keys)

		pyglet.resource.path= ['resources']
		pyglet.resource.reindex()

		#requires initial scene to run
	
	def set_scene(self,new_scene):
		self.scene=new_scene
		self.scene.set_game(self)
		pyglet.clock.schedule_interval(self.scene.update, 0.017)
		#sets scene and sets its game

	def start(self,initial_scene):
		self.set_scene(initial_scene)
		#pyglet.clock.schedule_interval(self.scene.update, 0.017)
		pyglet.app.run()
		
		
		#launches app

	def on_draw(self):
		self.game_window.clear()

		
		self.scene.draw()
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) 
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		self.fps_display.draw()
		self.game_window.flip()
	# in screen coords	
	def on_mouse_press(self,x,y,button,modifiers):
		for i in self.scene.clickables:
			if i.is_coord_in_box(x,y):
				i.on_click()

