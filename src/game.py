import constants as c
from components.event_listener import GameEventListener



class Game:
    def __init__(self, display, event_manager, gui_manager, camera, clock, game_states, start_state):
        """
        Initialize the game.
        """
        self.display = display
        self.clock = clock
        self.camera = camera
        self.event_manager = event_manager
        self.gui_manager = gui_manager
        self.game_states = game_states
        self.start_state = start_state

        self.running = True

        self.listener = GameEventListener(self)
        self.event_manager.subscribe(self.listener.subscriptions, self.listener)


    def run(self):
        """
        Main game loop.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(c.FPS)

    def update(self):
        """
        Update the game state.
        """
        pass

    def render(self):
        """
        Render the game state.
        """
        pass    

    def handle_events(self):
        self.event_manager.get_events()