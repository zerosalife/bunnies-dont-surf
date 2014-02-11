import pygame

import random

import collections

from gameskeleton.vector import Vec2
import gameskeleton.constants as c
import gameskeleton.modes
import gameskeleton.entity_component as ec
import gameskeleton.resource


class DebugMode(gameskeleton.modes.GameMode):

    def __init__(self, game):
        gameskeleton.modes.GameMode.__init__(self, game)

        self.last_keys = collections.defaultdict(bool)
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        self.new_presses = set()
        self.score = 0
        self.score_pos_init = Vec2(c.SCORE_POS)

        base_pos = Vec2(0, 0)

        self.e_list = [ec.base.Entity(self, components=[
            ec.Position(Vec2(-280, 200)),]),]

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
