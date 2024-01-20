import random

from spaceship_game.scenes.scene import Scene


class Death(Scene):

    def enter(self):
        print(f"You died, {random.sample(("sad", "mysterious", "not my fault", "for now", "it is fine"), 1)[0]}.")
        exit(0)
