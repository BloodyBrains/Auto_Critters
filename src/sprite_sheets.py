from pygame import Surface
from constants import SPRITE_SIZE, ANIM_FRAME_SPEED 


class Animation:
    def __init__(self, name: str, frames: list[Surface], frame_duration: int):
        self.name = name
        self.frames = frames
        self.frame_duration = frame_duration
    

class SpriteSheet:
    def __init__(self, name: str):
        self.name = name
        self.image = None
        self.size = None
        self.animations = {} 

    def add_animation(self, name: str, frames: list[Surface], frame_duration: int=ANIM_FRAME_SPEED):
        """Add an animation to the sprite sheet.
        
        Arguments:
            name {str} -- The name of the animation.
            frames {list[Surface]} -- The frames of the animation.
            frame_duration {int} -- The duration of each frame in milliseconds.
        """
        self.animations[name] = Animation(name, frames, frame_duration)
    
