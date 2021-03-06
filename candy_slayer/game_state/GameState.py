import pygame


class GameState(object):
    """
    Parent class for individual game states to inherit from.

    Re-worked from the original code by iminurnamez
    at https://gist.github.com/iminurnamez/8d51f5b40032f106a847
    """
    def __init__(self, manager):
        """
        Initialize the game state.

        :param manager: game object manager
        """
        self.manager = manager
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 24)

    def can_quit(self):
        """
        Getter for the boolean quit variable.

        :return: true if the game can quit.
        """
        return self.quit

    def is_done(self):
        """
        Getter for the boolean done variable.

        :return: true if the state is done.
        """
        return self.done

    def set_done(self, done):
        """
        Setter for the boolean done variable.

        :param done: boolean value for if the state is done.
        """
        self.done = done

    def get_persist(self):
        """
        Getter for the persistent data.

        :return: persist dict with data to be passed.
        """
        return self.persist

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        :param persistent: a dict passed from state to state
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.

        :param event: pygame event
        """
        pass

    def update(self, dt):
        """
        Update the state. Called by the Game object once per frame.

        :param dt: time since last frame
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen.

        :param surface: game screen
        """
        pass
