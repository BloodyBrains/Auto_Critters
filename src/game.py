from pygame import display as pg_display

import constants as c
from components.event_listener import GameEventListener
import game_states
import battle_maps.maps



class Game:    
    def __init__(self, display, event_manager, gui_manager, render_manager, clock):
        """
        Initialize the game.
        """
        self.display = display
        self.clock = clock
        self.event_manager = event_manager
        self.gui_manager = gui_manager
        self.render_manager = render_manager

        self.state_mgr = game_states.StateManager(self)

        self.running = True

        self.listener = GameEventListener(self)
        self.event_manager.subscribe(self.listener) 

        self.game_states = {
            'start': game_states.MainMenuState,
            'battle': game_states.BattleState
        }       

        for id, state in self.game_states.items():
            self.state_mgr.add_state(id, state)

        self.state_mgr.set_state('start')
        #self.active_state = self.game_states[c.START_STATE]


    def run(self):
        """
        Main game loop.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            pg_display.update()
            self.clock.tick(c.FPS)

    def update(self):
        """
        Update the game state.
        """
        self.active_state.update()

    def render(self):
        """
        Render the game state.
        """
        self.display.fill(c.BLACK)
        self.active_state.render()    

    def handle_events(self):
        self.event_manager.handle_events()


    def get_states(self):
        """
        Get the game states.
        """
        pass

    @property
    def active_state(self):
        """
        Get the active state.
        """
        return self._active_state
    
    @active_state.setter
    def active_state(self, state):
        """
        Set the active state.
        """
        self._active_state = state