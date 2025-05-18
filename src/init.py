import pygame

import constants as c
from game import Game
from camera import Camera
from events import EventManager
from game_states import StateManager
from gui import GUIManager
from render import RenderManager

# Initialize Pygame
pygame.init()

def get_display():
    """
    Create the display surface for the game.
    """
    c.MONITOR_SIZE = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    return pygame.display.set_mode(c.DISPLAY_SIZE)

def get_clock():
    """
    Create a clock object to control the frame rate.
    """
    return pygame.time.Clock()

def get_camera():
    """
    Create a camera object for the game.
    """
    return Camera()

def get_event_manager():
    """
    Create an event manager object for handling events.
    """
    return EventManager()

def get_gui_manager():
    """
    Create a GUI manager object for handling GUI elements.
    """
    return GUIManager()

def get_render_manager():
    """
    Create a render manager object for handling rendering.
    """
    return RenderManager()

def get_game_states(state_mgr):
    """
    Create a game states object for managing different game states.
    """
    for state in c.GAME_STATES:
        states = state_mgr.add_state(state, c.GAME_STATES[state])
    return states



