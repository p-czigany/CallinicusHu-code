from textwrap import dedent


class Engine(object):

    def __init__(self, scene_map):

        self.scene_map = scene_map
        self.next_scene = scene_map.opening_scene()
        self.scene_names = {
            "1": 'central_corridor',
            "2": 'laser_weapon_armory',
            "3": 'the_bridge',
            "4": 'escape_pod',
            "6": 'death',
            "5": 'finished',
        }

    def play(self):

        while True:
            if 'death' == self.next_scene.enter():
                self.next_scene = self.scene_map.next_scene('death')
            else:
                self.next_scene = self.scene_map.next_scene(self.move_freely())

    def move_freely(self):
        print(dedent("""Type the room's number into which you wish to go.
            1: Central Corridor
            2: Laser Weapon Armory
            3: The Bridge
            4: Escape Pod
            5: I just want to win.
            6: I just want to die.
            """))

        while True:
            target_room_code = input("< ")

            if self.next_scene == self.scene_map.scenes.get(self.scene_names.get(target_room_code)):
                print("Good news: You are already here. Dummy.")
            elif target_room_code.isnumeric() and 0 < int(target_room_code) < 7:
                return self.scene_names.get(target_room_code)
            else:
                print("Sorry you might had made a mistake, a typo or simply are retarded.")
