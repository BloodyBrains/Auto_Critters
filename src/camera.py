from pygame.locals import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

from constants import CAM_SPEED
from components.event_listener import CameraEventListener


class Camera:
    def __init__(self, event_manager):
        
        self.x_speed = 0
        self.y_speed = 0
        self.pos = (0, 0)
        self.is_active = True
        
        self.event_manager = event_manager
        self.listener = CameraEventListener(self)
        self.event_manager.subscribe(self.listener)


    def notify(self, event, **event_data):
        pass

    def activate(self):
        # Initialize the camera
        pass

    def deactivate(self):
        # Stop the camera
        pass

    def move(self, dx, dy):
        # Move the camera by dx, dy
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def update(self):
        self.pos = (self.pos[0] + self.x_speed, self.pos[1] + self.y_speed)