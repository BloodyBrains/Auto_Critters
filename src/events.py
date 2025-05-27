import pygame
import sys

from assets import load_assets
import constants
from components.event_listener import EventListener

class EventManager:
    def __init__(self):
        self.events = {}    #key: event type, value: list of listeners

        # Block all events by default
        pygame.event.set_blocked(None)

        # Allow only specific event types
        allowed_events = [pygame.QUIT, 
                          pygame.KEYDOWN, 
                          pygame.KEYUP, 
                          pygame.MOUSEBUTTONDOWN, 
                          pygame.MOUSEBUTTONUP]
                  
        pygame.event.set_allowed(allowed_events)
        pygame.event.clear()


    def handle_events(self):
        """
        Handles events from the pygame event queue.
        """
        for event in pygame.event.get():
            if event.type in self.events:
                self.notify(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    constants.FULL_SCREEN = not constants.FULL_SCREEN
                    if constants.FULL_SCREEN:
                        pygame.display.set_mode(constants.MONITOR_SIZE, pygame.FULLSCREEN)
                        #load_assets()
                    else:
                        pygame.display.set_mode(constants.DISPLAY_SIZE)
                elif event.key in self.events:
                    self.notify(event)
                elif event.key == pygame.K_SPACE:
                    constants.SPACE_PRESSED = 1
                    print(constants.SPACE_PRESSED)
            elif event.type == pygame.KEYUP:
                if event.key in self.events:
                    self.notify(event)          


    def subscribe(self, listener: EventListener):
        """
        Subscribe a listener (observer) to specific event types.
        """

        for event in listener.subscriptions:
            if event not in self.events:
                self.events[event] = []
            self.events[event].append(listener)



    def unsubscribe(self, event_types, listener):
        """
        Unsubscribe a listener from specific event types.
        """

        if not isinstance(event_types, list): # Ensure event_types is a list
            event_types = [event_types]

        for event in event_types:    
            if event_types in self.events and listener in self.events[event_types]:
                self.events[event_types].remove(listener)



    def notify(self, event):
        """
        Notify all listeners subscribed to a specific event type.
        """
        if event.type in self.events:
            for listener in self.events[event.type]:
                handled = listener.notify(event)
                if handled:
                    break
        elif event.type == pygame.KEYDOWN:
            for listener in self.events[event.key]:
                handled = listener.notify(event)
                if handled:
                    break
        elif event.type == pygame.KEYUP:
            for listener in self.events[event.key]:
                handled = listener.notify(event)
                if handled:
                    break

    def queue_event(self, custom_event_type, **event_data):
        """Queues a custom pygame.event.Event() object to the pygame event queue."""
        ev = pygame.event.Event(custom_event_type, event_data)
        pygame.event.post(ev)


# CUSTOM EVENT TYPES---------------------------------
EV_GRID_ROTATED_R = pygame.event.custom_type() #TODO: Consolidate this into one event a pass a clockwise flag

EV_GRID_ROTATED_L = pygame.event.custom_type()

    