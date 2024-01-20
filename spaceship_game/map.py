from spaceship_game.scenes.central_corridor import CentralCorridor
from spaceship_game.scenes.death import Death
from spaceship_game.scenes.escape_pod import EscapePod
from spaceship_game.scenes.finished import Finished
from spaceship_game.scenes.laser_weapon_armory import LaserWeaponArmory
from spaceship_game.scenes.the_bridge import TheBridge


class Map(object):

    def __init__(self):
        self.scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished(),
        }

    def set_start_scene(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    def __str__(self):
        return self.start_scene
