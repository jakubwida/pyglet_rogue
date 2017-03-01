from pyrogue_engine.utils.game import Game
from pyrogue_engine.utils.game_scene import GameScene
from pyrogue_engine.utils.layer import Layer
from pyrogue_engine.actors.actor_imple import *


game = Game()
game_scene = GameScene(game)

layer = Layer(game_scene)
actor = ActorImple(layer)


game.start(game_scene)


