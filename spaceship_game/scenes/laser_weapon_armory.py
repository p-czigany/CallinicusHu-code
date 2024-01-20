from textwrap import dedent

from spaceship_game.scenes import cypher_module
from spaceship_game.scenes.scene import Scene


def ask_for_password():
    return input("... ")


def guess_is_wrong(guess, password_encoded):
    return cypher_module.encode(guess) != password_encoded


class LaserWeaponArmory(Scene):
    ROUND_1_INTRO_TEXT = dedent(
        """
        The armory is locked behind a password.
        There is a password reminder sticked on the door.
            'Someone who is attracted to the homeless is a hobosexual.
            Someone who is attracted to the mexixans is a...'
        """
    )

    ROUND_1_PASSWORD_ENCODED = "kvwil ksrov"

    ROUND_1_FAIL_TEXT = "Your password appears to be incorrect."

    ROUND_1_WIN_TEXT = "You were right!"

    ROUND_2_INTRO_TEXT = dedent("""
        You have another chance but the air is running out of the room.
        Luckily you found another password reminder sticker.
        It says...
        
        kvwil ksrov

        Might be some sort of code.""")

    ROUND_2_PASSWORD_ENCODED = "ivwkz mwz"

    ROUND_2_FAIL_TEXT = "It might be something else. How much air..."

    ROUND_2_WIN_TEXT = "You were right this time!"

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
        if guess_is_wrong(guess, LaserWeaponArmory.ROUND_1_PASSWORD_ENCODED):
            print(LaserWeaponArmory.ROUND_1_FAIL_TEXT)

        else:
            print(LaserWeaponArmory.ROUND_1_WIN_TEXT)
            self.unlock()
            return

        print(LaserWeaponArmory.ROUND_2_INTRO_TEXT)
        guess = ask_for_password()
        if guess_is_wrong(guess, LaserWeaponArmory.ROUND_2_PASSWORD_ENCODED):
            print(LaserWeaponArmory.ROUND_2_FAIL_TEXT)
        else:
            print(LaserWeaponArmory.ROUND_2_WIN_TEXT)
            self.unlock()
            return

        raise Exception('death')

    def unlock(self):
        self.locked = False
