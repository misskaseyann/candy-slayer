import os
from random import randint

import pygame

from game_state.GameState import GameState


class BattleScreen(GameState):
    def __init__(self, manager):
        super().__init__(manager)

    def startup(self, persistent):
        self.house = self.manager.player.currhouse
        self.font1 = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 16)
        self.font2 = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 40)
        self.attk_color = (110, 84, 157)
        self.inv_color = (225, 149, 168)
        self.esc_color = (225, 149, 168)
        self.menu_num = 0
        self.curr_event = " "

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if self.menu_num == 0:
                    self.menu_num += 1
                    self.attk_color = (225, 149, 168)
                    self.inv_color = (110, 84, 157)
                    self.esc_color = (225, 149, 168)
                elif self.menu_num == 1:
                    self.menu_num += 1
                    self.attk_color = (225, 149, 168)
                    self.inv_color = (225, 149, 168)
                    self.esc_color = (110, 84, 157)
            if event.key == pygame.K_a:
                if self.menu_num == 2:
                    self.inv_color = (110, 84, 157)
                    self.esc_color = (225, 149, 168)
                    self.menu_num -= 1
                elif self.menu_num == 1:
                    self.attk_color = (110, 84, 157)
                    self.inv_color = (225, 149, 168)
                    self.menu_num -= 1
            if event.key == pygame.K_RETURN:
                if self.menu_num == 0:
                    if self.manager.neighborhood.get_population() == 0:
                        pygame.mixer.music.stop()
                        self.next_state = "WINNER"
                        self.done = True
                    elif self.house.get_population() == 0:
                        self.curr_event = "You saved the household. Time to move on..."
                    else:
                        self.manager.player.attack_monsters(self.house.monsters)
                        random = randint(0, len(self.house.monsters)) - 1
                        self.house.monsters[random].attack(self.manager.player)
                        if self.house.monsters[random].name == "Person":
                            self.curr_event = str(self.house.monsters[random].name) + " gives the player healing candy!"
                        else:
                            self.curr_event = str(self.house.monsters[random].name) + " attacks the player!"
                        if self.manager.player.currhp < 1:
                            pygame.mixer.music.stop()
                            self.next_state = "GAMEOVER"
                            self.done = True
                if self.menu_num == 1:
                    self.next_state = "INVENTORY"
                    self.done = True
                if self.menu_num == 2:
                    pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "eerieloop.wav"))
                    pygame.mixer.music.play(-1)
                    self.next_state = "NEIGHBORHOOD"
                    self.done = True

    def draw(self, surface):
        surface.fill((255, 241, 235))
        self.enemies_txt = self.font1.render("Monsters: " + str(self.manager.population) + "  |  Health: " +
                                             str(self.manager.player.currhp) + "/" + str(self.manager.player.hpmax) +
                                             "  |  Weapon: " + str(self.manager.player.currweapon.get_name()),
                                             True, (112, 89, 154))
        self.event_txt = self.font1.render(self.curr_event, True, (112, 89, 154))
        self.attack_txt = self.font2.render("Attack ", True, self.attk_color)
        self.inv_txt = self.font2.render("Inventory ", True, self.inv_color)
        self.esc_txt = self.font2.render("Escape", True, self.esc_color)
        surface.blit(self.enemies_txt, (300 - self.enemies_txt.get_width() / 2, 10))
        surface.blit(self.event_txt, (300 - self.event_txt.get_width() /2, 60))
        surface.blit(self.attack_txt, (300 - (self.attack_txt.get_width() + self.inv_txt.get_width() +
                                              self.esc_txt.get_width()) / 2, 460))
        surface.blit(self.inv_txt, (300 - self.inv_txt.get_width() / 2, 460))
        surface.blit(self.esc_txt, (300 + self.inv_txt.get_width() / 2, 460))
        for index, monster in enumerate(self.house.monsters):
            self.hp_text = self.font1.render("HP: " + "%.f" % monster.hp + "/" + str(monster.maxhp), True, (112, 89, 154))
            if index < 5:
                surface.blit(monster.monsterimg, ((index * 100) + 50, 130))
                surface.blit(self.hp_text, ((index * 100) + 50, 110))
            else:
                surface.blit(monster.monsterimg, (((index - 5) * 100) + (320 - (500) / 2), 300))
                surface.blit(self.hp_text, (((index - 5) * 100) + (320 - (500) / 2), 280))