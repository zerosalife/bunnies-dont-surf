if __name__ == '__main__':
    import gameskeleton.game

    game = gameskeleton.game.Game()

    # import gameskeleton.modes.debug.mode
    # game.mode = gameskeleton.modes.debug.mode.DebugMode(game)

    game.loop()
