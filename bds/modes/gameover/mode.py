import pygame

from bds.vector import Vec2
import bds.constants as c
import bds.modes
import bds.entity_component as ec
import bds.resource

class GameOverMode(bds.modes.GameMode):
    def __init__(self, game, score):
        bds.modes.GameMode.__init__(self, game)

        self.score = score

        self.e_list = []

    def render(self):
        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        for e in self.e_list:
            e.render()
