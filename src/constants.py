#DISPLAY--------------------------------------------------------
FULL_SCREEN = False
SCALE = 1
FPS = 60

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

#Game state information
START_SCREEN = "start"
BATTLE_STATE = "battle"
GAME_STATES = [START_SCREEN,
               BATTLE_STATE]
START_STATE = GAME_STATES[0]

