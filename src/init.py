import pygame

import constants as c
from game import Game
from camera import Camera
from events import EventManager
from gui import GUIManager

# Initialize Pygame
pygame.init()

def get_display():
    """
    Create the display surface for the game.
    """
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

def get_game_states():
    """
    Create a game states object for managing different game states.
    """
    return c.GAME_STATES



