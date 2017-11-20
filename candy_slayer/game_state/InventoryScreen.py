import pygame
import os

from game_state.GameState import GameState


class InventoryScreen(GameState):
    def __init__(self, manager):
        super().__init__(manager)

    def startup(self, persistent):
        self.font1 = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 13)
        self.font2 = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 16)
        self.inv_txt = self.font2.render("Player Inventory  |  Select Weapon", True, (112, 89, 154))
        self.x = 70
        self.y = 120
        self.weaponsel = 0

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if self.x < (((len(self.manager.player.inventory)/2) - 1) * 100) + 70:
                    self.weaponsel += 1
                    self.x += 100
                elif self.y < 250:
                    self.weaponsel += 1
                    self.x = 70
                    self.y = 250
                else:
                    self.weaponsel = 0
                    self.x = 70
                    self.y = 120
            if event.key == pygame.K_a:
                if self.x > 70:
                    self.weaponsel -= 1
                    self.x -= 100
                elif self.y > 120:
                    self.weaponsel -= 1
                    self.x = (((len(self.manager.player.inventory)/2) - 1) * 100) + 70
                    self.y = 120
            if event.key == pygame.K_RETURN:
                self.manager.player.currweapon = self.manager.player.inventory[self.weaponsel]
                self.next_state = "BATTLE"
                self.done = True


    def draw(self, surface):
        surface.fill((255, 241, 235))
        surface.blit(self.inv_txt, (300 - self.inv_txt.get_width() / 2, 10))
        for index, item in enumerate(self.manager.player.inventory):
            self.item_text = self.font1.render(item.name, True, (112, 89, 154))
            self.item_atk = self.font1.render("Atk: " + "%.2f" %
                                             (self.manager.player.attack * item.attack_mod), True, (112, 89, 154))
            self.item_uses = self.font1.render("Uses: " + str(item.num_uses), True, (112, 89, 154))
            if index < 5:
                surface.blit(item.img, ((index * 100) + (320 - (500)/2), 120))
                surface.blit(self.item_text,
                             ((index * 100) + (320 - (500)/2), 190))
                surface.blit(self.item_atk,
                             ((index * 100) + (320 - (500) / 2), 205))
                surface.blit(self.item_uses,
                             ((index * 100) + (320 - (500) / 2), 218))
            else:
                surface.blit(item.img, (((index - 5) * 100) + (320 - (500) / 2), 250))
                surface.blit(self.item_text,
                             (((index - 5) * 100) + (320 - (500) / 2), 320))
                surface.blit(self.item_atk,
                             (((index - 5) * 100) + (320 - (500) / 2), 335))
                surface.blit(self.item_uses,
                             (((index - 5) * 100) + (320 - (500) / 2), 348))
        pygame.draw.rect(surface, (112, 89, 154), (self.x, self.y, 68, 68), 5)