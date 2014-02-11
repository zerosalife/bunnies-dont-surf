import pygame
import pygame.locals as pgl
import vector

GAME_NAME = "Game Skeleton"
SCREEN_DIMENSIONS = vector.Vec2(768, 576)
TARGET_FPS = 60

BACKGROUND_COLOR = pygame.Color("0x000000")

VALID_ACTIONS = ["space"]

KEY_MAPPING = {
    pgl.K_SPACE: "space",
}

SCORE_POS = vector.Vec2(SCREEN_DIMENSIONS.x / 2, 20)

RES_IMAGES = {

}

RES_FONTS = {

}
