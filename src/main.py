import sys
import pygame

import constants as c
import init
import game
from components.event_listener import GameEventListener


# Main game loop
def main():
    # Initialization
    screen = init.get_display()
    clock = init.get_clock()    
    camera = init.get_camera()
    event_manager = init.get_event_manager()    
    gui_manager = init.get_gui_manager()
    game_states = init.get_game_states()    


    # Instantiate the Game object with dependencies
    game_controller = game.Game(
        screen,
        event_manager,
        gui_manager,
        camera,
        clock,
        game_states,
        c.START_STATE
    )

    # Start the game loop
    game_controller.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()