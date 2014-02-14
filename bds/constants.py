import pygame
import pygame.locals as pgl
import vector

GAME_NAME = "Bunnies Don't Surf"
SCREEN_DIMENSIONS = vector.Vec2(320, 480)
TARGET_FPS = 60
DT = 1/30.                                      # Physics fps

GRAVITY = vector.Vec2(0, 9) * 1000
TERMINAL_VELOCITY = vector.Vec2(0, 90)
BUNNY_JUMP = vector.Vec2(0, -20) * 1000
WALL_VELOCITY = vector.Vec2(-90, 0)

BACKGROUND_COLOR = pygame.Color("0x000000")     # Black
UI_TEXT_COLOR = pygame.Color("0xFFFFFF")        # White
BUNNY_COLOR = pygame.Color(215, 215, 215)       # Grey
WATER_COLOR = pygame.Color(91, 168, 255)        # Blue
FLOOR_COLOR = pygame.Color(92, 60, 13)          # Brown
WALL_COLOR = FLOOR_COLOR

BUNNY_DIMS = vector.Vec2(18, 12)
WATER_DIMS = vector.Vec2(98, 480)
FLOOR_DIMS = vector.Vec2(320, 80)
WALL_WIDTH = 60

WATER_POS = vector.Vec2(40, 240)
GAME_OVER_POS = vector.Vec2(SCREEN_DIMENSIONS.x / 2, 20)
GAME_OVER_SCORE_POS = vector.Vec2(SCREEN_DIMENSIONS.x / 2, 100)
SCORE_POS = vector.Vec2(SCREEN_DIMENSIONS.x / 2, 0)
FPS_POS = vector.Vec2(0, 0)

WALL_SPAWN_X = 400
WALL_DESPAWN_X = -10
CEILING_Y = -20

WALL_SPAWN_TIMER_MAX = 180

WALL_HEIGHT_LIMITS = (260, 400)
WALL_GAP_LIMITS = (85, 110)                 # Easier
# WALL_GAP_LIMITS = (30, 100)               # Hard as hell

VALID_ACTIONS = ["space"]

KEY_MAPPING = {
    pgl.K_SPACE: "space",
}


RES_IMAGES = {

}

RES_FONTS = {
    "small_gui": ("data/fonts/PressStart2P-Regular.ttf", 13),
    "med_gui": ("data/fonts/PressStart2P-Regular.ttf", 16),
}
