from abc import ABC, abstractmethod
from pygame.locals import QUIT

class EventListener(ABC):
    """
    Abstract base class for event listeners.
    """

    @abstractmethod
    def on_event(self, event):
        """
        Handle an event.

        :param event: The event to handle.
        """
        pass

    @abstractmethod
    def notify(self, event):
        """
        Notify the listener of an event.

        :param event: The event to notify.
        """
        pass



class GameEventListener(EventListener):
    """
    Concrete implementation of an event listener for the Game controller.
    """
    def __init__(self, game):
        """
        Initialize the GameEventListener.

        :param game: The game instance to notify.
        :param subscriptions: A list of event types to subscribe to.
        """
        self.game = game
        self.subscriptions = [QUIT]

    def on_event(self, event):
        """
        Handle a game event.

        :param event: The game event to handle.
        """
        pass


    def notify(self, event, *args, **kwargs):
        """
        Notify the listener of a game event.
        """
        
        if event.type == QUIT:
            self.game.running = False