import pygame

import random

import collections

from itertools import chain

from bds.vector import Vec2
import bds.constants as c
import bds.modes
import bds.entity_component as ec
import bds.resource
import bds.modes.gameover.mode
from bds import util

class DebugMode(bds.modes.GameMode):

    def __init__(self, game):
        bds.modes.GameMode.__init__(self, game)

        self.last_keys = collections.defaultdict(bool)
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        self.new_presses = set()

        self.score = 0
        self.score_pos_init = Vec2(c.SCORE_POS)

        self.collisionp = False

        self.player = ec.base.Entity(self, components=[
            ec.Rect(pygame.Rect(Vec2(80, 100), c.BUNNY_DIMS), c.BUNNY_COLOR),
            ec.Position(Vec2(80, 100)),
            ec.PlayerMovement()])

        self.floor = ec.base.Entity(self, components=[
            ec.Rect(pygame.Rect(Vec2(160, 440), c.FLOOR_DIMS), c.FLOOR_COLOR),
            ec.Position(Vec2(160, 440)),
            ec.Collider(),])

        self.wall_list = [
        # Wall bottom
            ec.base.Entity(self, components=[
                ec.Rect(pygame.Rect(Vec2(400,   # WALL_SPAWN_X
                                         370),  # WALL_BOT_HEIGHT
        # Wall Dims
                                    Vec2(60, c.SCREEN_DIMENSIONS.y - 370)),
                                    c.WALL_COLOR),
                ec.Position(Vec2(400, 370)),
                ec.WallMovement(),
                ec.Collider(),
            ]),
        ]


        self.e_list = list(util.flatten([
        # Water
            ec.base.Entity(self, components=[
                ec.Rect(pygame.Rect(Vec2(40, 240), c.WATER_DIMS), c.WATER_COLOR),
                ec.Position(Vec2(40, 240)),]),
        # # Walls
            self.wall_list,
        # # Wall bottom
        #     ec.base.Entity(self, components=[
        #         ec.Rect(pygame.Rect(Vec2(400,   # WALL_SPAWN_X
        #                                  370),  # WALL_BOT_HEIGHT
        # # Wall Dims
        #                             Vec2(80, c.SCREEN_DIMENSIONS.y - 370)),
        #                             c.WALL_COLOR),
        #         ec.Position(Vec2(400, 370)),
        #         ec.WallMovement(),
        #         ec.Collider(),
        #     ]),

        # Floor
            self.floor,
        # Bunny
            self.player,
            ]))

        self.fps_font = bds.resource.font.med_gui


    def finish(self):
        # Consider putting the movement of the player to the floor in
        # the GameOverMode, so we can animate the player falling.
        p_pos = self.player.handle("get_position")
        floor_rect = self.floor.handle("get_rect")
        if p_pos.y > floor_rect.top:
            self.player.handle("set_position",
                               Vec2(p_pos.x,
                                    floor_rect.top - c.BUNNY_DIMS.y / 2))
        self.game.mode = bds.modes.gameover.mode.GameOverMode(self.game,
                                                              self.score,
                                                              self.e_list)

    def update(self, time_elapsed):
        input = self.game.input
        self.valid_keys = [k for k, v in c.KEY_MAPPING.items()]
        self.pressed_keys = input.pressed_keys.copy()

        self.new_presses = set(k for k, v in self.pressed_keys.items() if v !=
                               self.last_keys[k] and v)

        for e in self.e_list:
            e.update(time_elapsed)

        if self.collisionp:
            print "Collided"
            self.finish()


        self.last_keys = self.pressed_keys


    def render(self):

        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        for e in self.e_list:
            e.render()

        fps = self.fps_font.render("{0:.1f}".format(self.game.clock.get_fps()),
                                   True, c.UI_TEXT_COLOR)
        scr.blit(fps, c.FPS_POS.as_tuple())
