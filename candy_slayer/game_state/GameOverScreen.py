import os
import pygame
from game_state.GameState import GameState


class GameOverScreen(GameState):
    """
    Title font: Alagard
    """
    def __init__(self, manager):
        super().__init__(manager)
        self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "gameover.png")).convert()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.title_img, (600,540)), (0,0))
