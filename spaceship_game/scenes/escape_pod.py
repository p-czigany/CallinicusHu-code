from spaceship_game.scenes.scene import Scene


class EscapePod(Scene):

    def enter(self):
        print("Here is the Escape Pod.")
        return 'go_anywhere'
