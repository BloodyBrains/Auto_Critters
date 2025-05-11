import pygame
import sys
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


    def get_events(self):
        """
        Handles events from the pygame event queue.
        """
        for event in pygame.event.get():
            if event.type in self.events:
                self.notify(event)            


    def subscribe(self, event_types, listener: EventListener):
        """
        Subscribe a listener (observer) to specific event types.
        """

        if not isinstance(event_types, list): # Ensure event_types is a list
            event_types = [event_types]

        for event in event_types:
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

    