import pygame

import collections


class Entity(object):
    def __init__(self, mode, components=[]):
        self.mode = mode
        self.components = components

    def handle(self, event, *extra_args):
        for component in self.components:
            ret = component.handle(self, event, *extra_args)

            if ret is not None:
                return ret

    def update(self, time_elapsed):
        self.handle("update", time_elapsed)

    def render(self):
        self.handle("render")

    def __repr__(self):
        return "<Entity components=[{0}]>".format(
            ", ".join(c.__repr__() for c in self.components))


class Component(object):
    def __init__(self):
        self.handlers = collections.defaultdict(list)

    def handle(self, entity, event, *extra_args):
        for handler in self.handlers[event]:
            ret = handler(self, entity, event, *extra_args)
            if ret is not None:
                return ret

    def register_handler(self, handler, name=None):
        if not name:
            name = handler.func_name

        self.handlers[name].append(handler)
