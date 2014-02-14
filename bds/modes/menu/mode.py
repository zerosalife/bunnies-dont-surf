import pygame

import bds

import bds.modes.debug.mode
from bds.vector import Vec2
import bds.constants as c
import bds.entity_component as ec


class MenuMode(bds.modes.GameMode):
    def __init__(self, game):
        bds.modes.GameMode.__init__(self, game)

        self.main_font = bds.resource.font.small_gui

        # self.logo = ec.base.Entity(self, components=[
        # ])
        self.logo_top = self.main_font.render("Bunnies Don't Surf",
                                              True, c.UI_TEXT_COLOR)
        self.instructions = self.main_font.render("Tap SPACE to hop.",
                                                  True, c.UI_TEXT_COLOR)
        self.logo_bottom = self.main_font.render("Press SPACE to start.",
                                                 True, c.UI_TEXT_COLOR)


    def play(self):
        self.game.mode = bds.modes.debug.mode.DebugMode(self.game)

    def update(self, time_elapsed):
        input = self.game.input
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        pressed_keys = input.pressed_keys.copy()

        self.new_presses = set(k for k, v in pressed_keys.items() if v !=
                               self.last_keys[k] and v)

        if self.game.input.state.space:
            self.play()

        self.last_keys = pressed_keys


    def render(self):
        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        # self.logo.render()
        scr.blit(self.logo_top, (c.SCREEN_DIMENSIONS.x / 2 - 120, 100))
        scr.blit(self.instructions, (c.SCREEN_DIMENSIONS.x / 2 - 110, 200))
        scr.blit(self.logo_bottom, (c.SCREEN_DIMENSIONS.x / 2 - 125, 350))
