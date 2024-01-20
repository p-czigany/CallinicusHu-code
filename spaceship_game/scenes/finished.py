from spaceship_game.scenes.scene import Scene


class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        exit(0)
