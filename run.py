if __name__ == '__main__':
    import bds.game

    game = bds.game.Game()

    import bds.modes.menu.mode
    game.mode = bds.modes.menu.mode.MenuMode(game)

    game.loop()
