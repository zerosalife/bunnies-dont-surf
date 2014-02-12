from bds.entity_component.base import Component

from bds.vector import Vec2

from pygame import draw, Color


class Rect(Component):
    def __init__(self, rect, color=Color("0xFFFFFF")):
        Component.__init__(self)

        self.rect = rect
        self.color = color

        self.register_handler(self.get_rect)
        self.register_handler(self.render)

    def get_rect(self, component, entity, event):
        return self.rect

    def set_rect(self, component, entity, event, value):
        self.rect = rect

    def render(self, component, entity, event):
        position = entity.handle("get_position")
        self.rect.center = position

        surf = entity.mode.game.screen
        draw.rect(surf, self.color, self.rect)
