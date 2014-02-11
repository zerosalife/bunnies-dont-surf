import pygame
import pygame.locals as pgl

import gameskeleton.constants as c

import collections


class Input(object):
    def __init__(self, game, keymap=c.KEY_MAPPING):
        self.game = game
        self.keymap = keymap

        self.keys = {k: False for k in c.VALID_ACTIONS}
        self.pressed_keys = collections.defaultdict(bool)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pgl.QUIT or \
                    (event.type == pgl.KEYDOWN and event.key == pgl.K_ESCAPE):
                self.game.running = False

            elif event.type == pgl.KEYDOWN and event.key in self.keymap:
                self.pressed_keys[event.key] = True
                self.keys[self.keymap[event.key]] = True

            elif event.type == pgl.KEYUP and event.key in self.keymap:
                self.pressed_keys[event.key] = False
                self.keys[self.keymap[event.key]] = False

    def next_frame(self):
        return InputState(state)

    @property
    def state(self):
        return InputState(self.keys.copy())


class InputState(object):
    def __init__(self, keys):
        self.keys = keys

    def __getattr__(self, name):
        if name in self.keys:
            return self.keys[name]
        else:
            raise AttributeError(name)
