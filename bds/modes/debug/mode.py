import pygame

import random

import collections

from bds.vector import Vec2
import bds.constants as c
import bds.modes
import bds.entity_component as ec
import bds.resource


class DebugMode(bds.modes.GameMode):

    def __init__(self, game):
        bds.modes.GameMode.__init__(self, game)

        self.last_keys = collections.defaultdict(bool)
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        self.new_presses = set()
        self.score = 0
        self.score_pos_init = Vec2(c.SCORE_POS)

        base_pos = Vec2(0, 0)

        self.e_list = [ec.base.Entity(self, components=[
            ec.Position(Vec2(-280, 200)),]),]

        self.fps_font = bds.resource.font.med_gui


    def update(self, time_elapsed):
        input = self.game.input
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        pressed_keys = input.pressed_keys.copy()

        self.new_presses = set(k for k, v in pressed_keys.items() if v !=
                               self.last_keys[k] and v)

        for e in self.e_list:
            e.update(time_elapsed)

        self.last_keys = pressed_keys


    def render(self):

        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        for e in self.e_list:
            e.render()

        fps = self.fps_font.render("{0:.1f}".format(self.game.clock.get_fps()),
                                   True, c.UI_TEXT_COLOR)
        scr.blit(fps, c.FPS_POS.as_tuple())
