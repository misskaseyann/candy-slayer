import os
import pygame
from game_state.GameState import GameState


class TitleScreen(GameState):
    """
    Title game state.

    Font credit: Alagard @ https://www.dafont.com/alagard.font
    """
    def __init__(self, manager):
        """
        Initialize the title game state.

        :param manager: game object manager
        """
        super().__init__(manager)
        self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "maintitle.png")).convert()
        self.next_state = "NEIGHBORHOOD"
        pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "title.wav"))
        pygame.mixer.music.play(-1)
        self.need_inst = True

    def get_event(self, event):
        """
        Event handling during the state.

        :param event: event to handle
        """
        # If player exits, quit the game.
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            # Enter button advances player to the instruction screen the first time, the game a second time.
            if event.key == pygame.K_RETURN:
                if self.need_inst:
                    self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "howto.png")).convert()
                    self.need_inst = False
                else:
                    pygame.mixer.music.stop()
                    self.done = True

    def draw(self, surface):
        """
        Surface the game objects are drawn on.

        :param surface: game screen
        """
        surface.blit(pygame.transform.scale(self.title_img, (600, 540)), (0, 0))
