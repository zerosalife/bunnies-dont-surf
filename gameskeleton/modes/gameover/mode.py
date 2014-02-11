import pygame

from gameskeleton.vector import Vec2
import gameskeleton.constants as c
import gameskeleton.modes
import gameskeleton.entity_component as ec
import gameskeleton.resource

class GameOverMode(gameskeleton.modes.GameMode):
    def __init__(self, game, score):
        gameskeleton.modes.GameMode.__init__(self, game)

        self.score = score

        self.e_list = []

    def render(self):
        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        for e in self.e_list:
            e.render()
