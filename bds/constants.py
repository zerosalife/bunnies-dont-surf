import pygame
import pygame.locals as pgl
import vector

GAME_NAME = "Game Skeleton"
SCREEN_DIMENSIONS = vector.Vec2(320, 480)
TARGET_FPS = 60
DT = 1/30.                                               # Physics fps

GRAVITY = vector.Vec2(0, 9) * 1000
TERMINAL_VELOCITY = vector.Vec2(0, 90)
BUNNY_JUMP = vector.Vec2(0, -20) * 1000

BACKGROUND_COLOR = pygame.Color("0x000000")
UI_TEXT_COLOR = pygame.Color("0xFFFFFF")
BUNNY_COLOR = pygame.Color(215, 215, 215)
WATER_COLOR = pygame.Color(91, 168, 255)

VALID_ACTIONS = ["space"]

KEY_MAPPING = {
    pgl.K_SPACE: "space",
}

SCORE_POS = vector.Vec2(SCREEN_DIMENSIONS.x / 2, 20)
FPS_POS = vector.Vec2(0, 0)

RES_IMAGES = {

}

RES_FONTS = {
    "med_gui": ("data/fonts/PressStart2P-Regular.ttf", 16),
}

BUNNY_DIMS = vector.Vec2(36, 24)
