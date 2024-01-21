from textwrap import dedent

from spaceship_game.scenes import cypher_module
from spaceship_game.scenes.scene import Scene

MAX_ATTEMPTS = 2
INTRO_TEXTS = [dedent("""
        The armory is locked behind a password.
        There is a password reminder sticked on the door.
            'Someone who is attracted to the homeless is a hobosexual.
            Someone who is attracted to the mexixans is a...'
        """), dedent("""
        You have another chance but the air is running out of the room.
        Luckily you found another password reminder sticker.
        It says...

        kvwil ksrov

        Might be some sort of code.""")]
ENCODED_PASSWORDS = ["kvwil ksrov", "ivwkz mwz"]
FAIL_TEXTS = ["Your password appears to be incorrect.", "It might be something else. How much air..."]
WIN_TEXTS = ["You were right!", "You were right this time!"]


def ask_for_password():
    return input("... ")


class LaserWeaponArmory(Scene):

    def __init__(self):
        super().__init__()
        self.locked = True

    def enter(self):
        print("This is the Laser Weapon Armory.")
        # if self.locked:
        self.spring_trap()

    def spring_trap(self):
        attempt_index = 0
        while self.locked:
            if attempt_index == MAX_ATTEMPTS:
                raise Exception('death')
            self.try_to_unlock(attempt_index)
            attempt_index += 1

    def try_to_unlock(self, attempt_index):
        print(INTRO_TEXTS[attempt_index])
        guess = ask_for_password()
        if cypher_module.encode(guess) != ENCODED_PASSWORDS[attempt_index]:
            print(FAIL_TEXTS[attempt_index])
        else:
            print(WIN_TEXTS[attempt_index])
            self.unlock()

    def unlock(self):
        self.locked = False
