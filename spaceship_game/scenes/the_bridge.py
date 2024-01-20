from spaceship_game.scenes.scene import Scene


class TheBridge(Scene):

    def enter(self):
        print("This is the Bridge.")
        return 'go_anywhere'
