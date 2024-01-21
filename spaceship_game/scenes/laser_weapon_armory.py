from textwrap import dedent

from spaceship_game.scenes import cypher_module
from spaceship_game.scenes.scene import Scene


def ask_for_password():
    return input("... ")


def guess_is_wrong(guess, password_encoded):
    return cypher_module.encode(guess) != password_encoded


class LaserWeaponArmory(Scene):
    MAX_ROUNDS = 2
    INTRO_TEXTS = [dedent(
        """
        The armory is locked behind a password.
        There is a password reminder sticked on the door.
            'Someone who is attracted to the homeless is a hobosexual.
            Someone who is attracted to the mexixans is a...'
        """
    ), dedent("""
        You have another chance but the air is running out of the room.
        Luckily you found another password reminder sticker.
        It says...
        
        kvwil ksrov

        Might be some sort of code."""
              )]
    ENCODED_PASSWORDS = ["kvwil ksrov", "ivwkz mwz"]
    FAIL_TEXTS = ["Your password appears to be incorrect.", "It might be something else. How much air..."]
    WIN_TEXTS = ["You were right!", "You were right this time!"]

    def __init__(self):
        super().__init__()
        self.locked = True

    def enter(self):
        print("This is the Laser Weapon Armory.")
        if self.locked:
            self.spring_trap()

    def spring_trap(self):
        round_index = 0
        while self.locked:
            if round_index == LaserWeaponArmory.MAX_ROUNDS:
                raise Exception('death')
            self.play_trap_round(round_index)
            round_index += 1

    def play_trap_round(self, round_index):
        print(LaserWeaponArmory.INTRO_TEXTS[round_index])
        guess = ask_for_password()
        if guess_is_wrong(guess, LaserWeaponArmory.ENCODED_PASSWORDS[round_index]):
            print(LaserWeaponArmory.FAIL_TEXTS[round_index])
        else:
            print(LaserWeaponArmory.WIN_TEXTS[round_index])
            self.unlock()

    def unlock(self):
        self.locked = False
