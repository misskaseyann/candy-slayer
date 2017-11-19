import os
import pygame
from game_state.GameState import GameState


class NeighborhoodScreen(GameState):
    def __init__(self, manager):
        super().__init__(manager)

    def startup(self, persistent):
        self.font = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 16)
        self.house_img = pygame.image.load(os.path.join("candy_slayer/assets/", "house.png")).convert_alpha()
        self.player_img = pygame.image.load(os.path.join("candy_slayer/assets/", "player.png")).convert_alpha()
        self.neighborhoodx = self.manager.neighborhood.width
        self.neighborhoody = self.manager.neighborhood.height
        self.playerx = (335 - ((self.manager.neighborhood.width * 100)/2))
        self.playery = (300 - ((self.neighborhoody * 80)/2))
        pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "eerieloop.wav"))
        pygame.mixer.music.play(-1)
        self.enemies_txt = self.font.render("Monsters: " + str(self.manager.population), True, (112, 89, 154))

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if self.playerx < (((self.neighborhoodx - 1) * 100) + (320 - ((self.neighborhoodx * 100)/2))):
                    self.playerx += 100
            if event.key == pygame.K_a:
                if self.playerx > (320 - (((self.neighborhoodx - 1) * 100)/2)):
                    self.playerx -= 100
            if event.key == pygame.K_w:
                if self.playery > (280 - (((self.neighborhoody - 1) * 80)/2)):
                    self.playery -= 80
            if event.key == pygame.K_s:
                if self.playery < (((self.neighborhoody - 1) * 80) + (280 - ((self.neighborhoody * 80)/2))):
                    self.playery += 80

    def draw(self, surface):
        surface.fill((255, 241, 235))
        for h in range(0, self.neighborhoody):
            for w in range(0, self.neighborhoodx):
                surface.blit(pygame.transform.scale(self.house_img, (64, 64)),
                             ((w * 100) + (320 - ((self.neighborhoodx * 100)/2)),
                              (h * 80) + (280 - ((self.neighborhoody * 80)/2))))
        surface.blit(self.player_img, (self.playerx, self.playery))
        surface.blit(self.enemies_txt, (300 - self.enemies_txt.get_width() / 2, 10))