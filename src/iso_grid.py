from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_TAB
import pygame

import constants as c
from components.event_listener import IsoGridEventListener
from assets import battlestate_sprites, grid_tile_sprites, elevation_sprites
from events import EV_GRID_ROTATED_L, EV_GRID_ROTATED_R

class Tile:
    """Represents a tile in the isometric grid."""
    def __init__(self, iso_pos, cart_pos, sprite, elevation=0):
        self.iso_pos = iso_pos  # Isometric position (row, col)
        self.pos = cart_pos  # Cartesian position (x, y)
        self.sprite = sprite  # Sprite image for the tile
        self.elevation = elevation  # Elevation level of the tile

    def __repr__(self):
        return f"Tile(iso_pos={self.iso_pos}, elevation={self.elevation})"

class IsoGrid:
    def __init__(self, map_data, event_manager):
        self.tile_width = c.TILE_WIDTH
        self.tile_height = c.TILE_HEIGHT
        self.tile_sprites = grid_tile_sprites
        self.wall_sprites = elevation_sprites
        self.map_data = map_data
        # Get the maximum elevation from the map data
        self.max_elevation = max(tile[1] for row in self.map_data for tile in row)
        self.full_map_surf = None
        
        self.listener = IsoGridEventListener(self)
        self.event_manager = event_manager               
        self.event_manager.subscribe(self.listener)
        self.render_list = []  # ((sprite, position), ...)
        self.pos = (0, 0)
        self.tiles = {}  # {(iso_pos): Tile object}
        self.selected_tile = None  # Currently selected tile on the map
        self.tile_selected_sprite = battlestate_sprites['tile_selected']

        # Precompute rotated versions of map_data
        self.map_data_rotated = [
            self.map_data,
            self._rotate_map(self.map_data, clockwise=True),
            self._rotate_map(self._rotate_map(self.map_data, clockwise=True), clockwise=True),
            self._rotate_map(self.map_data, clockwise=False),
        ]

        #self.rows_cols = (len(self.map_data[0]), len(self.map_data[0][0]))
        self.rows_cols = (len(self.map_data), len(self.map_data[0]))

        self.rotation_index = 0  # Start with the default rotation (0°)

        #self.start_x = c.CAM_STARTX
        #self.start_y = c.CAM_STARTY
        self.assemble_map()  # Assemble the render list

    
    def set_tile_map(self, map_data):
        """Set the Battle Grid map data."""
        self.map_data = map_data

    def _rotate_map(self, map_data, clockwise=True):
        """Helper function to rotate the map_data 90 degrees."""
        if clockwise:
            return [list(row) for row in zip(*map_data[::-1])]
        else:
            return [list(row) for row in zip(*map_data)][::-1]

    def rotate_grid(self, clockwise=True):
        """Switch to the next rotation of the grid."""
        if clockwise:
            self.rotation_index = (self.rotation_index + 1) % 4
        else:
            self.rotation_index = (self.rotation_index - 1) % 4

        # Rotate the selected tile if it exists
        if self.selected_tile:
            # Remove the previously selected tile sprite from the render list
            selected_tile_index = self.render_list.index((self.selected_tile.sprite, self.selected_tile.pos))
            self.render_list.pop(selected_tile_index + 1)


            old_row, old_col = self.selected_tile.iso_pos

            # Calculate the new position based on the rotation direction
            if clockwise:
                new_row = old_col
                new_col = len(self.map_data[0]) - 1 - old_row
            else:  # Counterclockwise
                new_row = len(self.map_data) - 1 - old_col
                new_col = old_row

            # Update the selected_tile's position
            #self.select_tile((new_row, new_col))
            self.selected_tile.iso_pos = (new_row, new_col)
            self.selected_tile.pos = self.iso_to_cart(self.selected_tile.iso_pos)

        self.assemble_map()  # Reassemble the map based on the new rotation

        self.event_manager.queue_event(EV_GRID_ROTATED_R, rotation_index=self.rotation_index)



    def assemble_map(self):
        """Assemble the Tile objects and render list by iterating through the active map_data."""
        self.tiles.clear()  # Clear the tiles dictionary
        self.render_list = []  # Clear the render list
        active_map_data = self.map_data_rotated[self.rotation_index]  # Use the active rotated map

        tile_layers = [[] for _ in range(self.max_elevation + 1)]  # Holds unsorted (tile_sprite, (x, y)) tuples for each elevation level
        wall_layers = [[] for _ in range(self.max_elevation + 1)]  # Holds unsorted (wall_sprite, (x, y)) tuples for each elevation level

        for ri, row in enumerate(active_map_data):
            for ci, tile in enumerate(row):
                if tile[0] == 0:  # Valid tile
                    # Handle wall sprites for elevation levels > 0
                    for elevation in range(0, tile[1]):
                        cart_x = (ci * c.TILE_WIDTH_HALF) + (ri * c.TILE_WIDTH_HALF)
                        cart_y = -(ci * c.TILE_HEIGHT_HALF) + (ri * c.TILE_HEIGHT_HALF)
                        cart_y -= (elevation) * c.TILE_ELEVATION

                        surf = self.wall_sprites['elevated_1']  # Example wall sprite
                        wall_layers[elevation].append((surf, (cart_x, cart_y)))

                    # Handle tile sprite
                    cart_x = (ri * c.TILE_WIDTH_HALF) + (ci * c.TILE_WIDTH_HALF)
                    cart_y = (ri * c.TILE_HEIGHT_HALF) - (ci * c.TILE_HEIGHT_HALF)
                    cart_y -= tile[1] * c.TILE_ELEVATION

                    surf = self.tile_sprites['dirtsand']  # Example tile sprite
                    tile_layers[tile[1]].append((surf, (cart_x, cart_y)))

        # Sort and append each layer to the render_list
        for elevation in range(self.max_elevation + 1):
            tile_layers[elevation].sort(key=lambda item: item[1][1])  # Sort by y position
            wall_layers[elevation].sort(key=lambda item: item[1][1])  # Sort by y position

            self.render_list.extend(tile_layers[elevation])
            self.render_list.extend(wall_layers[elevation])

        # Insert the selected_tile
        if self.selected_tile:
            selected_tile_index = self.render_list.index((self.selected_tile.sprite, self.selected_tile.pos))
            self.render_list.insert(selected_tile_index + 1, (self.tile_selected_sprite, self.selected_tile.pos))

        # Blit all the tiles onto a single surface for easier rendering
            # Determine the size of the Surface rect
        width = self.rows_cols[0] * self.tile_width
        height = self.rows_cols[1] * self.tile_height
        y_offset = (self.tile_height // 2) * (self.rows_cols[1] - 1)

            # Create a new surface for the full map
        self.full_map_surf = pygame.Surface((width, height))
        self.full_map_surf.set_colorkey((0, 0, 0))  
        self.full_map_surf.fill((0, 0, 0))

            # Blit each tile onto the full map surface
        for sprite, pos in self.render_list:
            adjusted_pos = (pos[0], pos[1] + y_offset)
            self.full_map_surf.blit(sprite, adjusted_pos)



    def iso_to_cart(self, iso_pos, width=0, height=0, with_offset=0):
        """Takes an isometric grid position and returns the screen coords
                of the top-left corner of the tile.
            If width, height args are passed, they are used to center a
                sprite on the tile
        
        Arguments:
            iso_pos {(int, int)} -- isometric grid postion to convert
            tile_elevation {int} -- elevation of the tile, used to adjust y pos
            width {int} ----------- width of image to be centered on tile
            height {int} ---------- height of image to be centered on tile
            with_offset {int} ----- if 1, will adjust the position based on camera offset
        """
        if not with_offset == 1:
        # set creature pos to top-left corner of tile
        #<TO DO: factor this: width(x + y)
            cart_x = (iso_pos[0] * c.TILE_WIDTH_HALF) + (iso_pos[1] * c.TILE_WIDTH_HALF)
            cart_y = (iso_pos[0] * c.TILE_HEIGHT_HALF) - (iso_pos[1] * c.TILE_HEIGHT_HALF)
            tile_elevation = self.get_tile_data(iso_pos)  # Get elevation from map_data
            cart_y -= tile_elevation[1] * c.TILE_ELEVATION


            # adjust position based on sprite size relative to center of tile
            # TO DO: adjust y pos to be slightly below center
            if not(width and height) == 0:
                cart_x += (c.TILE_WIDTH_HALF - (width / 2))
                cart_y += (c.TILE_HEIGHT_HALF - height)        

        '''
        # If we need the camera offset
        # Fix this: get the game.Battlestate.cam.pos and subtract it from cart_x, cart_y
        if with_offset != 0:
            cart_x += camera.Camera.offset_x
            cart_y += camera.Camera.offset_y
        '''
        return (cart_x, cart_y)
    
    
    def cart_to_iso(self, screen_pos, adjusted_for_cam = False):
        """
        Converts the screen position to the corresponding tile in the isometric grid.

        Args:
            screen_pos (tuple): The (x, y) position of the mouse.

        Returns:
            tuple: The (row, col) of the clicked tile, or None if out of bounds.
        """
        # Take a cart_pos and find which tile position it corresponds to for 0 elevation map
        # Find which

        x, y = screen_pos

        # Adjust for camera position if necessary
        if adjusted_for_cam == False:
            cam_pos = GlobalState.active_camera.pos
            x += cam_pos[0]
            y += cam_pos[1]

        # Convert Cartesian to isometric coordinates
        #row = int((y / c.TILE_HEIGHT_HALF) + (x / c.TILE_WIDTH_HALF) )
        #col = int((y / c.TILE_HEIGHT_HALF) - (x / c.TILE_WIDTH_HALF) )
        col = int((x / (c.TILE_WIDTH)) - (y / c.TILE_WIDTH_HALF))
        row = int((y / c.TILE_WIDTH_HALF) + (x / (c.TILE_WIDTH)))
        return row, col
    
    
    def select_tile(self, iso_pos):
        """Selects a tile based on its isometric position and returns the corresponding Tile object."""
        if self.selected_tile:
            # Remove the previously selected tile sprite from the render list
            selected_tile_index = self.render_list.index((self.selected_tile.sprite, self.selected_tile.pos))
            self.render_list.pop(selected_tile_index + 1)

        self.selected_tile = self.tiles.get(iso_pos)  # Use dictionary lookup
        if self.selected_tile:
            # Insert the tile_selected_sprite directly after the selected tile in the render_list
            selected_tile_index = self.render_list.index((self.selected_tile.sprite, self.selected_tile.pos))
            self.render_list.insert(selected_tile_index + 1, (self.tile_selected_sprite, self.selected_tile.pos))

        
        
    def get_tile_data(self, *tiles):
        """Returns the tile data for the specified tiles. Returns a list if 
        multiple tiles are provided, or a single tile data if only one tile 
        is provided."""

        tile_data = []
        for tile in tiles:
            row, col = tile
            if 0 <= row < len(self.map_data[self.rotation_index]) and 0 <= col < len(self.map_data[self.rotation_index][0]):
                tile_data.append(self.map_data[self.rotation_index][row][col])
            else:
                tile_data.append(None)
        return tile_data[0] if len(tile_data) == 1 else tile_data
        

    def sort_by_y(self, unsorted):
        """Sort the given list by the y-coordinate (cart_y) in ascending order."""
        return sorted(unsorted, key=lambda item: item[1][1])
    

    def render(self, game_win, cam_pos):
        """Renders a game-window sized rectangle of the pre-rendered map
        to the game window."""

        visible_rect = pygame.Rect(
            cam_pos[0], cam_pos[1], c.MONITOR_SIZE[0], c.MONITOR_SIZE[1])
        game_win.blit(self.full_map_surf, (0, 0), visible_rect)


    def update(self):
        pass


    def notify(self, event, **event_data):
        """Callback function from EventManager.post() to notify IsoGrid
            of potential click on a grid tile.
        
            Arguments:
                event {int} -- event type (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP)
                event_data {dict} -- event data (mouse_pos)
        """
        handled = False

        if event == pygame.MOUSEBUTTONDOWN:
            print("mouse down")
            print(event_data.get('event_data'))
            clicked_tile = self.check_tile_click(event_data.get('event_data')) 
            #tile_data = self.get_tile_data(clicked_tile)
            #events.queue_event(events.EV_TILE_CLICKED, clicked_tile = clicked_tile, tile_data = tile_data)
            events.queue_event(events.EV_TILE_CLICKED, clicked_tile = clicked_tile)
            handled = True
        elif event == pygame.MOUSEBUTTONUP:
            print("mouse up")
            handled = True

        elif event == pygame.K_TAB:
            # Rotate the grid when TAB is pressed
            self.rotate_grid()
            events.queue_event(events.EV_GRID_ROTATED_R, rotation_index=self.rotation_index)
            handled = True

        return handled


    def check_tile_click(self, mouse_pos):
        """
        Converts the mouse position to the corresponding tile in the isometric grid.

        Args:
            mouse_pos (tuple): The (x, y) position of the mouse.

        Returns:
            tuple: The (row, col) of the clicked tile, or None if out of bounds.
        """
        # Adjust mouse position based on grid offset
        x, y = mouse_pos
        cam_pos = GlobalState.active_camera.pos
        x += cam_pos[0]
        y += cam_pos[1]

        col = int((x / (c.TILE_WIDTH)) - (y / c.TILE_WIDTH_HALF))
        row = int((y / c.TILE_WIDTH_HALF) + (x / (c.TILE_WIDTH)))
        return row, col
    




    # Legacy code
    """

    # uses pygame.Surface.blits() to batch render each tile
    def render(self, game_win, cam_pos):
        adjusted_render_list = [
            (surf, (pos[0] - cam_pos[0], pos[1] - cam_pos[1]))
            for surf, pos in self.render_list
        ]

        game_win.blits(adjusted_render_list)
        
        
    """