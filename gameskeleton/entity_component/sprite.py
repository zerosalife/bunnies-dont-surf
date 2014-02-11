from gameskeleton.entity_component.base import Component

import math

import pygame
import pygame.locals as pgl

from gameskeleton.vector import Vec2


class Sprite(Component):
    def __init__(self, sprite, key_color=None):
        Component.__init__(self)

        self.key_color = key_color
        if self.key_color:
            self.sprite = sprite.convert()
        else:
            self.sprite = sprite

        self.register_handler(self.get_sprite)
        self.register_handler(self.set_sprite)
        self.register_handler(self.render)

    def get_sprite(self, component, entity, event):
        return self.sprite

    def set_sprite(self, component, entity, event, value):
        self.sprite = value

    def render(self, component, entity, event):

        position = entity.handle("get_position")

        sprite = self.sprite

        if self.key_color:
            self.sprite.set_colorkey(self.key_color, pygame.RLEACCEL)

        entity.mode.game.screen.blit(sprite, position.as_tuple)
