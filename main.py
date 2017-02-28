from pyrogue_engine.utils.game import Game
from pyrogue_engine.utils.scene import Scene
from pyrogue_engine.utils.layer import Layer
from pyrogue_engine.actors.actor_imple import *


game = Game()
scene = Scene(game)

layer = Layer(scene)
actor = ActorImple(layer)


game.start(scene)


