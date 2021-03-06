from pyrogue_engine.utils.game import Game
from pyrogue_engine.utils.game_scene import GameScene
from pyrogue_engine.utils.scene import Scene
from pyrogue_engine.utils.layer import Layer
from pyrogue_engine.actors.actor_imple import *
from pyrogue_engine.actors.menu_item import *

game = Game()
game_scene = GameScene(game)
menu_scene = Scene(game)

def set_game_scene():
	game.set_scene(game_scene)


layer = Layer(game_scene)
actor = ActorImple(layer)

menu_layer = Layer(menu_scene)
menu_item = MenuItem(menu_layer,"hello",40,50)
menu_item.set_function(set_game_scene)

game.start(menu_scene)


