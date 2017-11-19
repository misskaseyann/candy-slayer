import os
import pygame
from game_state.GameState import GameState


class TitleScreen(GameState):
    """
    Title font: Alagard
    """
    def __init__(self, manager):
        super().__init__(manager)
        self.title_img = pygame.image.load(os.path.join("candy_slayer/assets/", "maintitle.png")).convert()
        self.next_state = "NEIGHBORHOOD"

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.persist["screen_color"] = "black"
                self.done = True

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.title_img, (600,540)), (0,0))
