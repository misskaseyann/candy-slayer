import os
import pygame
from game_state.GameState import GameState


class NeighborhoodScreen(GameState):
    def __init__(self, manager):
        super().__init__(manager)

    def startup(self, persistent):
        self.bg_color = (255, 241, 235)
        self.house_img = pygame.image.load(os.path.join("candy_slayer/assets/", "house.png")).convert_alpha()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

    def draw(self, surface):
        surface.fill(self.bg_color)
        for h in range(0, self.manager.neighborhood.height):
            for w in range(0, self.manager.neighborhood.width):
                surface.blit(pygame.transform.scale(self.house_img, (64, 64)),
                             ((w * 100) + (320 - ((self.manager.neighborhood.width * 100)/2)), h * 80 + 20))
