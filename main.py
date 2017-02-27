from pyrogue_engine.utils.game import Game
from pyrogue_engine.utils.scene import Scene
from pyrogue_engine.utils.layer import Layer
from pyrogue_engine.actors.actor_imple import *

scene = Scene()
game = Game(scene)

layer = Layer()
actor = ActorImple()


scene.add_layer(layer)
layer.add_actor(actor)

game.start()


