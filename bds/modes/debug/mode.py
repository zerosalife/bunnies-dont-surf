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
        self.score_pos_init = Vec2(c.GAME_OVER_SCORE_POS)

        self.collisionp = False

        self.wall_spawn_timer = c.WALL_SPAWN_TIMER_MAX

        self.player = ec.base.Entity(self, components=[
            ec.Rect(pygame.Rect(Vec2(80, 100), c.BUNNY_DIMS), c.BUNNY_COLOR),
            ec.Position(Vec2(80, 100)),
            ec.PlayerMovement()])

        self.floor = ec.base.Entity(self, components=[
            ec.Rect(pygame.Rect(Vec2(160, 440), c.FLOOR_DIMS), c.FLOOR_COLOR),
            ec.Position(Vec2(160, 440)),
            ec.Collider(),])

        self.wall_list = self.make_wall()

        self.e_list = self.make_e_list()


        self.fps_font = bds.resource.font.med_gui

    def make_e_list(self):
        """Composites the entities in the correct order."""
        return list(util.flatten([
        # Water
            ec.base.Entity(self, components=[
                ec.Rect(pygame.Rect(c.WATER_POS, c.WATER_DIMS), c.WATER_COLOR),
                ec.Position(c.WATER_POS),]),
        # Walls
            self.wall_list,
        # Floor
            self.floor,
        # Bunny
            self.player,
            ]))

    def make_wall(self):
        bottom_wall_top = random.randint(c.WALL_HEIGHT_LIMITS[0],
                                         c.WALL_HEIGHT_LIMITS[1])
        wall_gap = random.randint(c.WALL_GAP_LIMITS[0],
                                  c.WALL_GAP_LIMITS[1])
        print wall_gap
        wall = [
        # Wall bottom
            ec.base.Entity(self, components=[
                ec.Rect(pygame.Rect(Vec2(c.WALL_SPAWN_X,
                                         bottom_wall_top),
        # Wall Dims
                                    Vec2(c.WALL_WIDTH,
                                         c.SCREEN_DIMENSIONS.y + wall_gap \
                                            - bottom_wall_top)),
                        c.WALL_COLOR),
                ec.Position(Vec2(c.WALL_SPAWN_X, bottom_wall_top + wall_gap / 2)),
                ec.WallMovement(),
                ec.Collider(),
                ]),
        # Wall top
            ec.base.Entity(self, components=[
                ec.Rect(pygame.Rect(Vec2(c.WALL_SPAWN_X,
                                         c.CEILING_Y),
                                    Vec2(c.WALL_WIDTH,
                                         bottom_wall_top - wall_gap)),
                        c.WALL_COLOR),
                ec.Position(Vec2(c.WALL_SPAWN_X, c.CEILING_Y)),
                ec.WallMovement(),
                ec.Collider(),
            ]),]
        print wall[0].handle("get_rect")
        print wall[1].handle("get_rect")
        return list(util.flatten(wall))


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
                                                              int(self.score),
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

        if self.wall_spawn_timer > 0:
            self.wall_spawn_timer -= 1
        else:
            # Spawn a wall
            self.wall_list.extend(self.make_wall())
            self.e_list = self.make_e_list()
            self.wall_spawn_timer = c.WALL_SPAWN_TIMER_MAX

        self.last_keys = self.pressed_keys


    def render(self):

        scr = self.game.screen

        scr.fill(c.BACKGROUND_COLOR)

        for e in self.e_list:
            e.render()

        fps = self.fps_font.render("{0:.1f}".format(self.game.clock.get_fps()),
                                   True, c.UI_TEXT_COLOR)
        score = self.fps_font.render("{0:d}".format(int(self.score)),
                                     True, c.UI_TEXT_COLOR, c.BACKGROUND_COLOR)
        scr.blit(fps, c.FPS_POS.as_tuple())
        scr.blit(score, c.SCORE_POS.as_tuple())
