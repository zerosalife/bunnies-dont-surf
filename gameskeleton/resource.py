import pygame

import gameskeleton.constants as c


class ResourceManager(object):

    def __init__(self, resource_def, load_fn):
        self.resource_def = resource_def
        self.load_fn = load_fn
        self.resource_cache = {k: None for k in self.resource_def.keys()}

    def __getattr__(self, name):
        if name in self.resource_def:

            if not self.resource_cache[name]:
                self.resource_cache[name] = \
                    self.load_fn(name, self.resource_def[name])

            return self.resource_cache[name]
        else:
            raise AttributeError("Resource not found: {0}".format(name))

image = ResourceManager(c.RES_IMAGES, lambda n, fn: pygame.image.load(fn))
font = ResourceManager(c.RES_FONTS, lambda n, fontdef:
                       pygame.font.Font(*fontdef))
