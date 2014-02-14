import pygame

from bds.vector import Vec2
import bds.constants as c
import bds.modes
import bds.entity_component as ec
import bds.resource

class GameOverMode(bds.modes.GameMode):
    def __init__(self, game, score, e_list):
        bds.modes.GameMode.__init__(self, game)

        self.score = score

        self.e_list = e_list

        self.buttons = []

        # self.overlay = [
        #     ec.base.Entity(self, components=[
        #         ec.
        #     ])
        # ]

        self.score_font = bds.resource.font.med_gui

        self.game_over_logo = self.score_font.render("GAME OVER",
                                                     True,
                                                     c.UI_TEXT_COLOR,
                                                     c.BACKGROUND_COLOR)
        self.score_logo = self.score_font.render("SCORE",
                                                 True,
                                                 c.UI_TEXT_COLOR,
                                                 c.BACKGROUND_COLOR)
        self.score = self.score_font.render("{0:d}".format(self.score),
                                            True,
                                            c.UI_TEXT_COLOR,
                                            c.BACKGROUND_COLOR)

    def render(self):
        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        for e in self.e_list:
            e.render()

        scr.blit(self.game_over_logo, c.GAME_OVER_POS)
        scr.blit(self.score_logo, c.GAME_OVER_SCORE_POS)
        scr.blit(self.score, c.GAME_OVER_SCORE_POS + Vec2(0, 40))
