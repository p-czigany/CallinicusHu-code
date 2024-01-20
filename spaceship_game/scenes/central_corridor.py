from spaceship_game.scenes.scene import Scene


class CentralCorridor(Scene):

    def enter(self):
        print("You are at the Central Corridor.")

        return 'go_anywhere'
