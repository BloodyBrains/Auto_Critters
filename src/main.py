import sys
import pygame

import constants as c
from assets import load_assets
import init
import game
from components.event_listener import GameEventListener
from game_states import StateManager


# Main game loop
def main():
    # Initialization

    screen = init.get_display()
    clock = init.get_clock()    
    event_manager = init.get_event_manager()    
    gui_manager = init.get_gui_manager()
    render_manager = init.get_render_manager()

    load_assets()

    # Instantiate the Game object with dependencies
    game_controller = game.Game(
        screen,
        event_manager,
        gui_manager,
        render_manager,
        clock,
    )

    # Start the game loop
    game_controller.run()

    pygame.display.quit()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()