from bds.entity_component.base import Component

from bds.vector import Vec2

import bds.constants as c


class Movement(Component):
    def __init__(self, velocity=Vec2(0, 0), acceleration=Vec2(0, 0)):
        Component.__init__(self)

        self.velocity = velocity
        self.acceleration = acceleration

        self.register_handler(self.update)

    def update(self, component, entity, event, time_elapsed):
        pass


class PlayerMovement(Movement):
    def __init__(self, velocity=Vec2(0, 0), acceleration=Vec2(0, 0)):
        Movement.__init__(self)

    def update(self, component, entity, event, time_elapsed):
        input = entity.mode.game.input

        valid_keys = entity.mode.valid_keys
        pressed_keys = entity.mode.pressed_keys
        new_presses = entity.mode.new_presses

        position = entity.handle("get_position")

        for k in valid_keys:
            if k in new_presses:
                if input.state.space:
                    self.acceleration = Vec2(0, 0)
                    self.velocity = c.BUNNY_JUMP * time_elapsed

        self.acceleration += c.GRAVITY * time_elapsed
        self.velocity += self.acceleration * time_elapsed
        if self.velocity.y > c.TERMINAL_VELOCITY.y:
            self.velocity = c.TERMINAL_VELOCITY
        position += self.velocity * time_elapsed

        if position.y < c.CEILING_Y:
            position.y = c.CEILING_Y

        entity.handle("set_position", position)



class WallMovement(Movement):
    def __init__(self, velocity=Vec2(0, 0), acceleration=Vec2(0, 0)):
        Movement.__init__(self)

        self.velocity = c.WALL_VELOCITY
        self.scored = False


    def update(self, component, entity, event, time_elapsed):
        position = entity.handle("get_position")

        position += self.velocity * time_elapsed

        entity.handle("set_position", position)

        rect = entity.handle("get_rect")

        p_pos = entity.mode.player.handle("get_position")

        if position.x + rect.width / 2 < p_pos.x and self.scored == False:
            entity.mode.score += 0.5
            self.scored = True

        if position.x < c.WALL_DESPAWN_X:
            entity.mode.wall_list.pop(0)
            entity.mode.e_list = entity.mode.make_e_list()
