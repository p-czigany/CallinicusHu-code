from textwrap import dedent

from spaceship_game.scenes import cypher_module
from spaceship_game.scenes.scene import Scene


class LaserWeaponArmory(Scene):
    def __init__(self):
        super().__init__()
        self.armory_locked = "Locked"

    def enter(self):
        print("This is the Laser Weapon Armory.")
        if self.armory_locked == "Locked":
            return self.open_lock()
        else:
            return 'go_anywhere'

    def open_lock(self):
        print(dedent("""
                            The armory is locked behind a password.
                            There is a password reminder sticked on the door.
                                'Someone who is attracted to the homeless is a hobosexual.
                                Someone who is attracted to the mexixans is a...'
                            """))

        password = cypher_module.encode(input("... "))

        if password != cypher_module.encode(cypher_module.decode("kvwil ksrov")):
            print(dedent(f"""
                            Your password appears to be incorrect.
                            You have another chance but the air is running out of the room.
                            Luckily you found another password reminder sticker.
                            It says...

                            kvwil ksrov

                            Might be some sort of code."""))

        else:
            print("You were right!")
            self.armory_locked = "Unlocked"
            return 'go_anywhere'

        password = cypher_module.encode(input("... "))

        if password != cypher_module.encode(cypher_module.decode("ivwkz mwz")):
            print("It might be something else. How much air...")
            return 'die'
        else:
            print("You were right this time!")
            self.armory_locked = "Unlocked"
            return 'go_anywhere'
