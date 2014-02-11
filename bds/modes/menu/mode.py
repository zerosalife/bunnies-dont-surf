import pygame

import bds

import bds.modes.debug.mode
from bds.vector import Vec2
import bds.constants as c
import bds.entity_component as ec


class MenuMode(bds.modes.GameMode):
    def __init__(self, game):
        bds.modes.GameMode.__init__(self, game)

        self.main_font = bds.resource.font.med_gui

        def play():
            self.game.mode = bds.modes.debug.mode.DebugMode(self.game)


        self.logo = ec.base.Entity(self, components=[
        ])


    def update(self, time_elapsed):
        input = self.game.input
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        pressed_keys = input.pressed_keys.copy()

        self.new_presses = set(k for k, v in pressed_keys.items() if v !=
                               self.last_keys[k] and v)

        if entity.mode.game.input.state.space:
            self.play()

        self.last_keys = pressed_keys


    def render(self):
        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        self.logo.render()
