import pygame.sprite

from components.animation_ctrl import Animation_Ctrl
from assets import dragon_sprites, shroom_sprites
from constants import SPACE_PRESSED
from creature_states import STATE_MAPPING

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from creature_states import State

class Creature(pygame.sprite.Sprite):

    def __init__(self, name, anim_ctrl: Animation_Ctrl, image=None, rect=None, groups=None):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = rect if rect else pygame.Rect(0, 0, 50, 50) 
        self.groups = groups if groups else []

        self.dirty = 1
        self.facing = 'sw'
        self.states = {}
        self.current_state = None
        self.iso_pos = None
        self.elevation = 0
        self.center_pos = None

        self.anim_ctrl = anim_ctrl
        self.anim_ctrl.setup(self)

    def __str__(self):
        return f"{self.name}"
    
    def render(self, game_win, cam_pos):
        """Render the creature to the game window.
        
        Arguments:
            game_win {[type]} -- [description]
            cam_pos {[type]} -- [description]
        """
        if self.dirty:
            game_win.blit(self.image, (self.pos[0] - cam_pos[0], self.pos[1] - cam_pos[1]))

    def set_elevation(self, amount):
        for i in range(len(self.elevation)):
             self.elevation[i] += amount

        print(f"Elevation set to: {self.elevation}")

    def update(self, dt):
        pass


    

class PuffCreature(Creature):
    state_ids = ['idle']

    def __init__(self, name, anim_ctrl, image=None, rect=None, groups=None):
        super().__init__(name, anim_ctrl, image, rect, groups)
        self.dirty = 1
        #self.facing = 'SE'
        self.current_state = None
        self.center_pos = None
        self.sprite_sheet = dragon_sprites['puff']

        self.image = self.sprite_sheet.animations['idle_sw'].frames[0]
        self.pos = (215, 208)

        for state in self.state_ids:
            self.states[state] = STATE_MAPPING[state](state, self, self.anim_ctrl.get_animation(state))

        """DEBUG"""
        self.jumping = True
        self.falling = False
        self.jump_h = 30
        self.jump_ctrl = 0
        self.jump_speed = 15
        self.curr_jump_h = 0
        """---------"""

    def update(self, dt):
        #pass
        """DEBUG"""
        from constants import SPACE_PRESSED
        if SPACE_PRESSED == 0:
            self.jump()
        else:
            print("Jumping")
        """---------"""


    def jump(self):
        if self.jump_ctrl == self.jump_speed:
            if self.jumping:
                if self.curr_jump_h < self.jump_h:
                    self.pos = (self.pos[0], self.pos[1] - 2)
                    self.curr_jump_h += 2
                    self.dirty = 1
                else:
                    self.jumping = False
                    self.falling = True
            else:
                if self.curr_jump_h > 0:
                    self.pos = (self.pos[0], self.pos[1] + 2)
                    self.curr_jump_h -= 2
                    self.dirty = 1
                else:
                    self.falling = False
                    self.jumping = True

            self.jump_ctrl = (self.jump_ctrl + 1) % (self.jump_speed + 1)
        else:
            self.dirty = 0
            self.jump_ctrl = (self.jump_ctrl + 1) % (self.jump_speed + 1)


class ShroomCreature(Creature):
    state_ids = ['idle']

    def __init__(self, name, anim_ctrl, image=None, rect=None, groups=None):
        super().__init__(name, anim_ctrl, image, rect, groups)
        self.dirty = 1
        #self.facing = 'SE'
        self.center_pos = None
        self.sprite_sheet = shroom_sprites['shroom_1']

        self.image = self.sprite_sheet.animations['idle_sw'].frames[0]
        self.pos = (310, 215)

        for state in self.state_ids:
            self.states[state] = STATE_MAPPING[state](state, self, self.anim_ctrl.get_animation(state))

        self.current_state = self.states['idle']
        self.current_state.enter()

        """DEBUG"""
        self.jumping = True
        self.falling = False
        self.jump_h = 30
        self.jump_ctrl = 0
        self.jump_speed = 15
        self.curr_jump_h = 0
        """---------"""

        """DEBUG"""
        self.elevation = []
        for i in range(0, len(self.image)):
            self.elevation.append(len(self.image) - i -1)

        print(f"Elevation set to: {self.elevation}")


    def update(self, dt):
        #pass
        """DEBUG"""
        from constants import SPACE_PRESSED
        if SPACE_PRESSED == 0:
            self.jump()
        else:
            print("Jumping")
        """---------"""

        self.current_state.update()
        self.anim_ctrl.update(dt)


    def jump(self):
        if self.jump_ctrl == self.jump_speed:
            if self.jumping:
                if self.curr_jump_h < self.jump_h: 
                    if self.curr_jump_h == 14:
                        self.set_elevation(1)
                    self.pos = (self.pos[0], self.pos[1] - 2)
                    self.curr_jump_h += 2
                    self.dirty = 1
                else:
                    self.jumping = False
                    self.falling = True
            else:
                if self.curr_jump_h > 0:
                    if self.curr_jump_h == 14:
                        self.set_elevation(-1)
                    self.pos = (self.pos[0], self.pos[1] + 2)
                    self.curr_jump_h -= 2
                    self.dirty = 1
                else:
                    self.falling = False
                    self.jumping = True

            self.jump_ctrl = (self.jump_ctrl + 1) % (self.jump_speed + 1)
        else:
            self.dirty = 0
            self.jump_ctrl = (self.jump_ctrl + 1) % (self.jump_speed + 1)
