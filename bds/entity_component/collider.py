from bds.entity_component.base import Component

from bds.vector import Vec2


class Collider(Component):
    def __init__(self):
        Component.__init__(self)

        self.register_handler(self.update)

    def update(self, component, entity, event, time_elapsed):
        rect = entity.handle("get_rect")

        p_rect = entity.mode.player.handle("get_rect")

        if rect.colliderect(p_rect):
            entity.mode.collisionp = True
