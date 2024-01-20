from spaceship_game.engine import Engine
from spaceship_game.map import Map

a_map = Map()
a_map.set_start_scene("central_corridor")
a_game = Engine(a_map)
a_game.play()

print("The End")
