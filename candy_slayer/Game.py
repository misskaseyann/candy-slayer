from Neighborhood import Neighborhood
from Player import Player
import pygame
from random import *


class Game(object):
    """
    Manages individual game states, the pygame logic,
    and the game loop.

    Re-worked from the original code by iminurnamez
    at https://gist.github.com/iminurnamez/8d51f5b40032f106a847
    """

    def __init__(self, screen, states, start_state):
        """
        Initialize the Game object.

        :param screen: the pygame display surface
        :param states: a dict mapping state-names to GameState objects
        :param start_state: name of the first active game state
        """
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        """Switch to the next game state."""
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        """
        Check for state flip and update active state.

        :param dt: milliseconds since last frame.
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw(self.screen)

    def run(self):
        """Game runtime is spent in this loop."""
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()
