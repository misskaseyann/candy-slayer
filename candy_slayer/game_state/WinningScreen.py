import os
import pygame

from game_state.GameState import GameState


class WinningScreen(GameState):
    """
    Winning game state.

    Font credit: Alagard @ https://www.dafont.com/alagard.font
    """
    def __init__(self, manager):
        """
        Initialize the winning game state.

        :param manager: game object manager
        """
        super().__init__(manager)
        self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "winner.png")).convert()

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        :param persistent: a dict passed from state to state
        """
        pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "winner.wav"))
        pygame.mixer.music.play(1)

    def get_event(self, event):
        """
        Event handling during the state.

        :param event: event to handle
        """
        # Quit the game when the player exits.
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            # Enter advances the screen to the credits.
            if event.key == pygame.K_RETURN:
                self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "credits.png")).convert()

    def draw(self, surface):
        """
        Surface the game objects are drawn on.

        :param surface: game screen
        """
        surface.blit(pygame.transform.scale(self.title_img, (600, 540)), (0, 0))
