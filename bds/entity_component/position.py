from bds.entity_component.base import Component


class Position(Component):
    def __init__(self, position):
        Component.__init__(self)
        self.position = position

        self.register_handler(self.get_position)
        self.register_handler(self.set_position)

    def get_position(self, component, entity, event):
        return self.position

    def set_position(self, component, entity, event, value):
        self.position = value
