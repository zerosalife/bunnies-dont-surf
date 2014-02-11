if __name__ == '__main__':
    import bds.game

    game = bds.game.Game()

    import bds.modes.debug.mode
    game.mode = bds.modes.debug.mode.DebugMode(game)

    game.loop()
