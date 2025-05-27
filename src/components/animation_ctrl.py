from pygame import Rect, Surface

from sprite_sheets import SpriteSheet
from animations import Animation


class Animation_Ctrl:
    def __init__(self, spritesheet: SpriteSheet):
        """Initialize the Animation Controller.
        Arguments:
            spritesheet {SpriteSheet} -- The sprite sheet containing the animations.
        """
        self.owner = None
        self.spr_sheet = spritesheet
        self.animations = {}
        self.current_animation = None
        self.current_frame = 0
        self.frame_duration = 0
        self.timer = 0

    def update(self, dt):
        """Update the animation frame.
        """
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.current_frame += 1
            if self.current_frame >= self.frame_count:
                self.current_frame = 0
            self.owner.image = self.current_animation.frames[self.current_frame]

    def setup(self, owner):
        """Setup the animation controller.
        """
        self.owner = owner
        self.extract_animations(self.spr_sheet)

    def extract_animations(self, sprite_sheet: SpriteSheet):
        """Extract animations from the sprite sheet.
        
        Arguments:
            sprite_sheet {SpriteSheet} -- The sprite sheet to extract animations from.
        """        
        for anim in sprite_sheet.animations.values():
            self.animations[anim.name] = Animation(anim.name, anim.frames, anim.frame_duration)


    def get_animation(self, name: str) -> Animation:
        """Get an animation by name.
        
        Arguments:
            name {str} -- The name of the animation.
        
        Returns:
            Animation -- The requested animation.
        """
        return self.animations.get(name)    
    
    def set_animation(self, animation_id: str, facing: str):
        """Set the current animation by ID.
        
        Arguments:
            animation_id {str} -- The ID of the animation to set.
            facing {str} -- The facing direction of the owner ('ne', 'se', 'sw', 'nw').
        """
        # Get the animation based on the ID and facing direction
        animation_id = f"{animation_id}_{facing}"

        if animation_id in self.animations:
            self.current_animation = self.animations[animation_id]
            self.current_frame = 0
            self.frame_count = self.current_animation.frame_count
            self.frame_duration = self.current_animation.frame_duration
            self.image = self.current_animation.frames[self.current_frame]
        else:
            raise ValueError(f"Animation '{animation_id}' not found.")
        
