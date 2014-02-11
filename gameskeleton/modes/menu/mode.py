import pygame

import gameskeleton

import gameskeleton.modes.debug.mode
from gameskeleton.vector import Vec2
import gameskeleton.constants as c
import gameskeleton.entity_component as ec


class MenuMode(gameskeleton.modes.GameMode):
    def __init__(self, game):
        gameskeleton.modes.GameMode.__init__(self, game)

        self.main_font = gameskeleton.resource.font.med_gui

        def play():
            self.game.mode = gameskeleton.modes.debug.mode.DebugMode(self.game)


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

        self.scr.fill(c.BACKGROUND_COLOR)

        self.logo.render()
