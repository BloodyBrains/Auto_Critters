import os

import pygame

import constants as c


# TODO: Refactor asset loading to use a more dynamic approach, possibly with a config file or JSON.
# TODO: Rmove hardcoded paths and use a more flexible asset management system.
#GUI ASSET PATHS-----------------------------------------------------
menu_paths = {}
menu_paths['turn_menu_button_blank'] = os.path.join(c.ASSETS_SPRITES, 'button_turn_menu_blank.png')

#CREATURE ASSET PATHS------------------------------------------------
air_paths = {}
air_paths['air'] = os.path.join(c.ASSETS_SPRITES, 'air.png')

battlestate_paths = {}
battlestate_paths['bgr'] = os.path.join(c.ASSETS_SPRITES, 'nebula_bgr.png')
battlestate_paths['tile_selected'] = os.path.join(c.ASSETS_SPRITES, 'tile_selected.png')

chaos_paths = {}
chaos_paths['chaos'] = os.path.join(c.ASSETS_SPRITES, 'chaos.png')

#GRID TILE ASSET PATHS--------------------------------------------
grid_tile_paths = {}
grid_tile_paths['dirtsand'] = os.path.join(c.ASSETS_SPRITES, 'tile_sanddirt.png')
debug_tile_paths = {}
debug_tile_paths['debug'] = os.path.join(c.ASSETS_SPRITES, 'debug_rect.png')

elevation_tile_paths = {}
elevation_tile_paths['elevated_1'] = os.path.join(c.ASSETS_SPRITES, 'tile_elevated_1.png')

#PLAYER ASSET PATHS--------------------------------------------------
player_paths = {}
player_paths['player'] = os.path.join(c.ASSETS_SPRITES, 'player_wizard.png')

#GAME STATE ASSET PATHS--------------------------------------------
rosteredit_paths = {}
rosteredit_paths['bgr'] = os.path.join(c.ASSETS_SPRITES, 'nebula_bgr.png')
rosteredit_paths['play'] = os.path.join(c.ASSETS_SPRITES, 'play_button.png')

main_menu_paths = {}
main_menu_paths['bgr'] = os.path.join(c.ASSETS_SPRITES, 'start_screen_bgr.png')
main_menu_paths['play'] = os.path.join(c.ASSETS_SPRITES, 'play_button.png')


# Load all sprites at once explicitly for now
air_sprites = {}
battlestate_sprites = {}
button_sprites = {}
chaos_sprites = {}
grid_tile_sprites = {}
debug_sprites = {}
elevation_sprites = {}
player_sprites = {}
rosteredit_sprites = {}
main_menu_sprites = {}
menu_sprites = {}


def load_assets():
    """Pre-loads game assets
    """
    
    for name, path in air_paths.items():
        air_sprites[name] = pygame.image.load(path).convert()
        air_sprites[name].set_colorkey((0, 0, 0))

    for name, path in battlestate_paths.items():
        battlestate_sprites[name] = pygame.image.load(path).convert()
        battlestate_sprites[name].set_colorkey((0, 0, 0))    

    for name, path in chaos_paths.items():
        chaos_sprites[name] = pygame.image.load(path).convert()
        chaos_sprites[name].set_colorkey((0, 0, 0))

    for name, path in grid_tile_paths.items():
        grid_tile_sprites[name] = pygame.image.load(path).convert()
        grid_tile_sprites[name].set_colorkey((0, 0, 0))

    for name, path in debug_tile_paths.items():
        debug_sprites[name] = pygame.image.load(path).convert()
        debug_sprites[name].set_colorkey((0, 0, 0))

    for name, path in elevation_tile_paths.items():
        elevation_sprites[name] = pygame.image.load(path).convert()
        elevation_sprites[name].set_colorkey((0, 0, 0))    

    for name, path in player_paths.items():
        player_sprites[name] = pygame.image.load(path).convert()
        player_sprites[name].set_colorkey((0, 0, 0))

    for name, path in rosteredit_paths.items():
        rosteredit_sprites[name] = pygame.image.load(path).convert()
        rosteredit_sprites[name].set_colorkey((0, 0, 0))

    for name, path in main_menu_paths.items():
        main_menu_sprites[name] = pygame.image.load(path).convert()
        main_menu_sprites[name].set_colorkey((0, 0, 0))

    #GUI assets
    for name, path in menu_paths.items():
        menu_sprites[name] = pygame.image.load(path).convert()
        menu_sprites[name].set_colorkey((0, 0, 0))