from pygame import Surface

from assets import main_menu_sprites
from battle_maps.maps import maps_data
from camera import Camera
from iso_grid import IsoGrid
#from constants import RENDER_LAYERS
#from components.renderable import Renderable

class GameState:
    def __init__(self, state_mgr, game_ctrl, event_manager, *args, **kwargs):
        self.state_mgr = state_mgr
        self.game_ctrl = game_ctrl
        self.event_manager = event_manager
        self.display = game_ctrl.display

    def enter(self):
        """
        Called when the state is entered.
        """
        pass

    def exit(self):
        """
        Called when the state is exited.
        """
        pass

    def handle_events(self, events):
        """
        Handle events for this state.
        """
        pass

    def update(self, dt):
        """
        Update the state logic.
        """
        pass

    def render(self):
        """
        Render the state to the screen.
        """
        pass


class StateManager:
    def __init__(self, owner):
        self.owner = owner
        self.event_mgr = owner.event_manager
        self.states = {}
        self.active_state = None

    def add_state(self, name, state):
        """
        Add a state to the manager.
        """
        self.states[name] = state

    def set_state(self, name, **kwargs):
        """
        Transition to a new state.
        """
        if self.active_state:
            self.active_state.exit()

        state_class = self.states.get(name)
        if state_class:
            self.active_state = state_class(self, self.owner, self.event_mgr, **kwargs)
            self.active_state.enter()

            # Set the active state of the owner
            self.owner.active_state = self.active_state

    def handle_events(self, events):
        """
        Delegate event handling to the active state.
        """
        if self.active_state:
            self.active_state.handle_events(events)

    def update(self, dt):
        """
        Delegate updating to the active state.
        """
        if self.active_state:
            self.active_state.update(dt)


class MainMenuState(GameState):
    def enter(self):
        """State Initialization"""
        self.bgr = main_menu_sprites['bgr']
        self.game_ctrl.display.blit(self.bgr, (0, 0))

        self.state_mgr.set_state(
            'battle', 
            map_data=maps_data['MAP_1']
        )

    def exit(self):
        print("Exiting Main Menu")

    def update(self, dt):
        """State Logic"""
        pass

    def handle_events(self, events):
        pass

    def render(self):
        pass



class BattleState(GameState):
    def __init__(self, state_mgr, game_ctrl, event_mgr, map_data=None):
        super().__init__(state_mgr, game_ctrl, event_mgr)
        self.map_data = map_data
        self.iso_grid = IsoGrid(self.map_data, self.event_manager)
        self.cam = Camera(self.event_manager)

    def enter(self):
        print("Entering Battle State")
        # Assemble the battle map

    def exit(self):
        print("Exiting Battle State")

    def handle_events(self, events):
        pass

    def update(self):
        self.cam.update()
        self.iso_grid.update()

    def render(self):
        self.iso_grid.render(self.game_ctrl.display, self.cam.pos)  

    def get_map_data(self):
        """
        Get the map data for the main menu.
        """
        return self.map_data 