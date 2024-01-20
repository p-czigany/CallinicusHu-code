from textwrap import dedent

from spaceship_game.scenes import cypher_module
from spaceship_game.scenes.scene import Scene


def ask_for_password():
    return input("... ")


def guess_is_wrong(guess, password_encoded):
    return cypher_module.encode(guess) != password_encoded


class LaserWeaponArmory(Scene):
    ROUND_1_INTRO_TEXT = dedent("""
                            The armory is locked behind a password.
                            There is a password reminder sticked on the door.
                                'Someone who is attracted to the homeless is a hobosexual.
                                Someone who is attracted to the mexixans is a...'
                            """)

    ROUND_2_INTRO_TEXT = dedent(f"""
                            Your password appears to be incorrect.
                            You have another chance but the air is running out of the room.
                            Luckily you found another password reminder sticker.
                            It says...

                            kvwil ksrov

                            Might be some sort of code.""")

    def __init__(self):
        super().__init__()
        self.locked = True

    def enter(self):
        print("This is the Laser Weapon Armory.")
        if self.locked:
            self.spring_trap()

    def spring_trap(self):
        print(LaserWeaponArmory.ROUND_1_INTRO_TEXT)

        guess = ask_for_password()
        if guess_is_wrong(guess, "kvwil ksrov"):
            print(LaserWeaponArmory.ROUND_2_INTRO_TEXT)

        else:
            print("You were right!")
            self.unlock()
            return

        guess = ask_for_password()
        if guess_is_wrong(guess, "ivwkz mwz"):
            print("It might be something else. How much air...")
            raise Exception('death')
        else:
            print("You were right this time!")
            self.unlock()

    def unlock(self):
        self.locked = False
