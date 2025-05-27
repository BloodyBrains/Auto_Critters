import os


#DISPLAY--------------------------------------------------------
FULL_SCREEN = False
MONITOR_SIZE = None # Set during initialization
SCALE = 1
FPS = 60
CAM_SPEED = 3

# Native resolution for 32-bit 2D graphics
NATIVE_WIDTH = 640
NATIVE_HEIGHT = 360

# Modern resolutions for scaling
FULL_HD_WIDTH = 1920
FULL_HD_HEIGHT = 1080
HD_WIDTH = 1280
HD_HEIGHT = 720

DISPLAY_WIDTH = NATIVE_WIDTH * SCALE
DISPLAY_HEIGHT = NATIVE_HEIGHT * SCALE
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

#ASSETS----------------------------------------------------
ASSETS_SPRITES = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets\sprites')
SPRITE_SIZE = (50, 50) # Default
ANIM_FRAME_SPEED = 300 # Default


#GAME STATES----------------------------------------------------
START_SCREEN = "start"
BATTLE_STATE = "battle"
GAME_STATES = [START_SCREEN,
               BATTLE_STATE]
START_STATE = GAME_STATES[0]

#RENDER LAYER----------------------------------------------------
RENDER_LAYERS = {
    "background": 0,
    "iso_grid":   1,
    "tile":       2,
    "tile_obj":   3,
    "agent":      4,
    "projectile": 5,
    "hud":        6,
    "gui":        7,
}

#TILE GRID----------------------------------------------------
#TILE_WIDTH = 192
#TILE_HEIGHT = 96
#TILE_SIZE = (TILE_WIDTH, TILE_HEIGHT)
#TILE_WIDTH_HALF = 96
#TILE_HEIGHT_HALF = 48
#TILE_ELEVATION = 16

TILE_WIDTH = 100
TILE_HEIGHT = 50
TILE_SIZE = (TILE_WIDTH, TILE_HEIGHT)
TILE_WIDTH_HALF = 50
TILE_HEIGHT_HALF = 25
TILE_ELEVATION = 20

# COLORS----------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
DARK_GRAY = (169, 169, 169)
LIGHT_GRAY = (211, 211, 211)
DARK_BLUE = (0, 0, 139)
DARK_GREEN = (0, 100, 0)
DARK_RED = (139, 0, 0)
DARK_PURPLE = (128, 0, 128)
DARK_CYAN = (0, 139, 139)
DARK_ORANGE = (255, 140, 0)
DARK_YELLOW = (255, 215, 0)

# DEBUG----------------------------------------------------
SPACE_PRESSED = 0

