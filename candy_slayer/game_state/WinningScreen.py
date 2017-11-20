import os
import pygame
from game_state.GameState import GameState


class WinningScreen(GameState):
    """
    Title font: Alagard
    """
    def __init__(self, manager):
        super().__init__(manager)
        self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "winner.png")).convert()

    def startup(self, persistent):
        pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "winner.wav"))
        pygame.mixer.music.play(1)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.title_img =pygame.image.load(os.path.join("candy_slayer/assets/", "credits.png")).convert()

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.title_img, (600,540)), (0,0))
