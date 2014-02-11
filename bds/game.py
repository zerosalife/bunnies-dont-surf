import sys

import pygame
import pygame.locals as pgl

import bds.constants as c
import bds.input

class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(tuple(c.SCREEN_DIMENSIONS))

        self.running = False
        self.mode = None

        self.input = bds.input.Input(self)

        self.tick = 0
        self.total_time = 0.0
        self.dt = 1/c.PHYSICS_FPS
        self.accumulator = 0.0

        pygame.display.set_caption(c.GAME_NAME)
        self.clock = pygame.time.Clock()
        self.current_time = self.clock.get_rawtime()

    def loop(self):
        self.running = True
        while self.running:
            self.clock.tick()
            self.new_time = self.clock.get_rawtime()
            self.frame_time = self.new_time - self.current_time
            self.current_time = self.new_time


            pygame.time.wait(1 / c.TARGET_FPS)
            time_elapsed = 1 / c.TARGET_FPS   # Duration per frame in ms

            self.input.handle_events()
            self.update(time_elapsed)
            self.render()
            print self.clock.get_fps()
        self.exit()

    def exit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def update(self, time_elapsed):
        self.tick += 1
        self.total_time += time_elapsed

        if self.mode:
            self.mode.update(time_elapsed)

    def render(self):
        if self.mode:
            self.mode.render()

        else:
            if self.input.state.space:
                self.screen.fill(c.BACKGROUND_COLOR)
            else:
                self.screen.fill(pygame.Color("0x7f0000"))

        pygame.display.update()
