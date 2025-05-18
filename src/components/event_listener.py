from abc import ABC, abstractmethod
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_TAB, K_ESCAPE

from constants import CAM_SPEED

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


class CameraEventListener(EventListener):
    """
    Concrete implementation of an EventListener.
    """
    def __init__(self, camera):
        self.camera = camera
        self.subscriptions = [K_UP, K_DOWN, K_LEFT, K_RIGHT]

    def on_event(self, event):
        pass

    def notify(self, event):
        """
        Notify the listener of a subscribed event.

        :param event: The event to notify.
        """
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.camera.y_speed = -CAM_SPEED  # Move up
                return True
            elif event.key == K_DOWN:
                self.camera.y_speed = CAM_SPEED  # Move down
                return True
            elif event.key == K_LEFT:
                self.camera.x_speed = -CAM_SPEED  # Move left
                return True
            elif event.key == K_RIGHT:
                self.camera.x_speed = CAM_SPEED  # Move right
                return True
        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                self.camera.y_speed = 0
                return True
            elif event.key == K_LEFT or event.key == K_RIGHT:
                self.camera.x_speed = 0
                return True
        else:
            return False



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
        self.subscriptions = [K_ESCAPE, QUIT]

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
        
        if event.type == QUIT or event.key == K_ESCAPE:
            self.game.running = False


class IsoGridEventListener(EventListener):
    """
    Concrete implementation of an event listener for the IsoGrid.
    """
    def __init__(self, grid):
        """
        Initialize the IsoGridEventListener.

        :param grid: The IsoGrid instance to notify.
        """

        self.grid = grid
        self.subscriptions = [MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_TAB]

    def on_event(self, event):
        """
        Handle an event.

        :param event: The event to handle.
        """
        pass

    def notify(self, event):
        """
        Notify the listener of an event.

        :param event: The event to notify.
        """
        if event.type == KEYDOWN:
            if event.key == K_TAB:
                self.grid.rotate_grid()
            