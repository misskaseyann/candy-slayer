import os
import pygame

from candy_slayer.game_state.GameState import GameState


class GameOverScreen(GameState):
    """
    Game over game state for losing the game.

    Music credit: Visager @ https://soundcloud.com/visagermusic
    Font credit: Alagard @ https://www.dafont.com/alagard.font
    """
    def __init__(self, manager):
        """
        Initialize the game over object.

        :param manager: game object manager
        """
        super().__init__(manager)
        self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "gameover.png")).convert()

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        :param persistent: a dict passed from state to state
        """
        pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "gameover.wav"))
        pygame.mixer.music.play(0)

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.

        :param event: event to be handled
        """
        if event.type == pygame.QUIT:
            self.quit = True

    def draw(self, surface):
        """
        Draw objects to the game screen.

        :param surface: the game screen
        """
        surface.blit(pygame.transform.scale(self.title_img, (600, 540)), (0, 0))
