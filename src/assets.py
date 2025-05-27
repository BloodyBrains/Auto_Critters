import os

import json
import pygame

import constants as c
import sprite_sheets


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
 
dragon_paths = {}
dragon_paths['puff'] = (os.path.join(c.ASSETS_SPRITES, 'puff_idle_sw.png'),
                        os.path.join(c.ASSETS_SPRITES, 'puff.json'))

shroom_paths = {}
#shroom_paths['shroom'] = (os.path.join(c.ASSETS_SPRITES, 'shroom.png'),
#                        os.path.join(c.ASSETS_SPRITES, 'shroom.json'))
shroom_paths['shroom_1'] = (os.path.join(c.ASSETS_SPRITES, 'shroom_1.png'),
                        os.path.join(c.ASSETS_SPRITES, 'shroom_1.json'))

#GRID TILE ASSET PATHS--------------------------------------------
grid_tile_paths = {}
grid_tile_paths['dirtsand'] = os.path.join(c.ASSETS_SPRITES, 'tile_sanddirt.png')
grid_tile_paths['dirt'] = os.path.join(c.ASSETS_SPRITES, 'tile_dirt.png')
debug_tile_paths = {}
debug_tile_paths['debug'] = os.path.join(c.ASSETS_SPRITES, 'debug_rect.png')

elevation_tile_paths = {}
elevation_tile_paths['elevated_1'] = os.path.join(c.ASSETS_SPRITES, 'tile_elevated_1.png')
elevation_tile_paths['elevation'] = os.path.join(c.ASSETS_SPRITES, 'tile_elevation.png')
elevation_tile_paths['tile_elevation_test'] = os.path.join(c.ASSETS_SPRITES, 'tile_elevation_test.png')

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
dragon_sprites = {}
shroom_sprites = {}
grid_tile_sprites = {}
debug_sprites = {}
elevation_sprites = {}
player_sprites = {}
rosteredit_sprites = {}
main_menu_sprites = {}
menu_sprites = {}


def create_spritesheet_WIP(file_data: 'json', image_path: str):
    """Takes a .json file and returns a SpriteSheet object.
    
    Arguments:
        file_data {[dict]} -- [.json file data]
        image_path {[str]} -- [Path to the image file]
    """
    sprite_sheet = sprite_sheets.SpriteSheet(file_data['meta']['image'])

    # Load the sprite sheet image
    sprite_sheet.image = pygame.image.load(image_path).convert_alpha()
    sprite_sheet.image.set_colorkey(c.BLACK)
    sprite_sheet.size = file_data['meta']['size']

    for tag in file_data['meta']['frameTags']:
        animation_name = tag['name']
        start_frame = tag['from']
        end_frame = tag['to']
        frames = []

        for i in range(start_frame, end_frame + 1):
            frame_name = list(file_data['frames'].keys())[i]
            frame_data = file_data['frames'][frame_name]['frame']
            rect = pygame.Rect(frame_data['x'], frame_data['y'], frame_data['w'], frame_data['h'])

            # Extract the full frame
            frame_surface = sprite_sheet.image.subsurface(rect)

            # Slice the frame into segments
            slices = []
            for slice_data in file_data['meta']['slices']:
                slice_rect = pygame.Rect(
                    slice_data['keys'][0]['bounds']['x'],  # X offset of the slice
                    slice_data['keys'][0]['bounds']['y'],  # Y offset of the slice
                    slice_data['keys'][0]['bounds']['w'],  # Width of the slice
                    slice_data['keys'][0]['bounds']['h']   # Height of the slice
                )
                slice_surface = frame_surface.subsurface(slice_rect)
                slices.append(slice_surface)

            # Store the slices for this frame
            frames.append(slices)

        # Add the animation to the SpriteSheet
        frame_duration = file_data['frames'][frame_name]['duration']
        sprite_sheet.add_animation(animation_name, frames, frame_duration)

    return sprite_sheet


def create_spritesheet(file_data, image_path):
    """Takes a .json file and returns a SpriteSheet object.
    
    Arguments:
        file_data {[dict]} -- [.json file data]
        image_path {[str]} -- [Path to the image file]
    """
    sprite_sheet = sprite_sheets.SpriteSheet(file_data['meta']['image'])

    sprite_sheet.image = pygame.image.load(image_path).convert()
    sprite_sheet.image.set_colorkey(c.BLACK)
    
    sprite_sheet.size = file_data['meta']['size']

    for tag in file_data['meta']['frameTags']:
        animation_name = tag['name']
        start_frame = tag['from']
        end_frame = tag['to']
        frames = []

        for i in range(start_frame, end_frame + 1):
            frame_name = list(file_data['frames'].keys())[i]
            frame_data = file_data['frames'][frame_name]['frame']
            rect = pygame.Rect(frame_data['x'], frame_data['y'], frame_data['w'], frame_data['h'])
            frame_surface = sprite_sheet.image.subsurface(rect)
            frames.append(frame_surface)

        frame_duration = file_data['frames'][frame_name]['duration']
        sprite_sheet.add_animation(animation_name, frames, frame_duration)

    return sprite_sheet


# LOAD ASSETS------------------------------------------------------------------

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

    for name, path in dragon_paths.items():
        data = None
        with open(path[1], "r") as f:
            data = json.load(f)
        dragon_sprites[name] = create_spritesheet(data, path[0])

    for name, path in shroom_paths.items():
        data = None
        with open(path[1], "r") as f:
            data = json.load(f)
        shroom_sprites[name] = create_spritesheet_WIP(data, path[0])

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


    '''
    for name, path in air_paths.items():
        air_sprites[name] = pygame.image.load(path).convert()
        air_sprites[name].set_colorkey((0, 0, 0))

    for name, path in battlestate_paths.items():
        battlestate_sprites[name] = pygame.image.load(path).convert()
        battlestate_sprites[name].set_colorkey((0, 0, 0))    

    for name, path in chaos_paths.items():
        chaos_sprites[name] = pygame.image.load(path).convert()
        chaos_sprites[name].set_colorkey((0, 0, 0))

    for name, path in dragon_paths.items():
        dragon_sprites[name] = pygame.image.load(path).convert()
        dragon_sprites[name].set_colorkey((0, 0, 0))

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
    '''

#--------------------------------------------------------------------END load_assets


# SpriteSheets Data--------------------------------------------------


