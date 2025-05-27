from __future__ import annotations
from abc import ABC, abstractmethod


from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from animations import Animation
    from creatures import Creature



class State(ABC):
    """Base class for all game states."""
    
    def __init__(self, name: str, owner: Creature, animations: List[Animation] = None):
        self.name = name
        self.owner = owner
        self.animations = animations
        self.curr_animation = None

    @abstractmethod
    def enter(self):
        """Called when the state is entered."""
        pass

    @abstractmethod
    def exit(self):
        """Called when the state is exited."""
        pass

    @abstractmethod
    def update(self):
        """Update the state logic."""
        pass

    def set_animation(self, animation_id: str):
        """Set the animation for the creature."""
        self.curr_animation = self.animations.get(animation_id)



class IdleState(State):
    """State representing the creature being idle."""
    
    def __init__(self, name: str, owner: Creature, animations: List[Animation]):
        super().__init__(name, owner, animations)

    def enter(self):
        """Set the creature to idle animation."""
        self.owner.anim_ctrl.set_animation("idle", self.owner.facing)

    def exit(self):
        """Reset any flags or states if necessary."""
        pass

    def update(self):
        """Update the idle state logic."""
        pass




STATE_MAPPING = {
    'idle': IdleState,
    # Add other states here as needed
}

    