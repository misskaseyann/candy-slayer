import os
from random import randint

import pygame

from candy_slayer.game_state.GameState import GameState


class BattleScreen(GameState):
    """
    Battle game state for all player vs monster battles.

    Music credit: Visager @ https://soundcloud.com/visagermusic
    Image credit: http://pixeljoint.com/pixelart/63772.htm
    Font credit: Alagard @ https://www.dafont.com/alagard.font
    """
    def __init__(self, manager):
        """
        Initialize the battle game state.

        :param manager: game object manager
        """
        super().__init__(manager)

    def startup(self, persistent):
        """
        Base-line initialization that needs to happen when the game state is in action.

        :param persistent: dictionary object
        """
        self.house = self.manager.player.currhouse
        self.font1 = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 16)
        self.font2 = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 40)
        self.attk_color = (110, 84, 157)
        self.inv_color = (225, 149, 168)
        self.esc_color = (225, 149, 168)
        self.menu_num = 0
        self.curr_event = " "
        self.player_event = " "

    def get_event(self, event):
        """
        Event handler.

        :param event: action to be handled
        """
        # Closing the window quits the program.
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            # Move the menu selection to the right.
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
            # Move the menu selection to the self.
            if event.key == pygame.K_a:
                if self.menu_num == 2:
                    self.inv_color = (110, 84, 157)
                    self.esc_color = (225, 149, 168)
                    self.menu_num -= 1
                elif self.menu_num == 1:
                    self.attk_color = (110, 84, 157)
                    self.inv_color = (225, 149, 168)
                    self.menu_num -= 1
            # Select the menu option highlighted.
            if event.key == pygame.K_RETURN:
                # Attack menu option.
                if self.menu_num == 0:
                    # Check if we won the game.
                    if self.manager.neighborhood.get_population == 0:
                        pygame.mixer.music.stop()
                        self.next_state = "WINNER"
                        self.done = True
                    # Check if we saved the people in the house.
                    elif self.house.get_population == 0:
                        self.curr_event = "You saved the household. Time to move on..."
                    else:
                        # Check if the weapon has any more usage.
                        if self.manager.player.currweapon.num_uses == 0:
                            self.player_event = "The " + str(self.manager.player.currweapon.name) + " is unusable!"
                        # Attack monsters in the house.
                        else:
                            self.manager.player.attack_monsters(self.house.monsters)
                            self.player_event = "You attack with the " + str(self.manager.player.currweapon.name) \
                                                + "..."
                        random = randint(0, len(self.house.monsters)) - 1
                        self.house.monsters[random].attack(self.manager.player)
                        # Check if a person gives the player candy.
                        if self.house.monsters[random].name == "Person":
                            self.curr_event = str(self.house.monsters[random].name) + " gives the player healing candy!"
                        # Show what monster attacked the player.
                        else:
                            self.curr_event = str(self.house.monsters[random].name) + " attacks the player!"
                        # End game if player health is 0.
                        if self.manager.player.currhp < 1:
                            pygame.mixer.music.stop()
                            self.next_state = "GAMEOVER"
                            self.done = True
                # Inventory menu option.
                if self.menu_num == 1:
                    self.next_state = "INVENTORY"
                    self.done = True
                # Escape menu option.
                if self.menu_num == 2:
                    pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "eerieloop.wav"))
                    pygame.mixer.music.play(-1)
                    self.next_state = "NEIGHBORHOOD"
                    self.done = True

    def draw(self, surface):
        """
        Draw any objects to the screen.

        :param surface: game screen
        """
        surface.fill((255, 241, 235))
        # Top GUI text stats.
        self.enemies_txt = self.font1.render("Monsters: " + str(self.manager.population) + "  |  Health: " +
                                             str(self.manager.player.currhp) + "/" + str(self.manager.player.hpmax) +
                                             "  |  Weapon: " + str(self.manager.player.currweapon.name),
                                             True, (112, 89, 154))
        # Top GUI text actions/event.
        self.event_txt = self.font1.render(self.curr_event, True, (112, 89, 154))
        self.player_txt = self.font1.render(self.player_event, True, (112, 89, 154))
        # Menu options.
        self.attack_txt = self.font2.render("Attack ", True, self.attk_color)
        self.inv_txt = self.font2.render("Inventory ", True, self.inv_color)
        self.esc_txt = self.font2.render("Escape", True, self.esc_color)
        # Text display.
        surface.blit(self.enemies_txt, (300 - self.enemies_txt.get_width() / 2, 10))
        surface.blit(self.event_txt, (300 - self.event_txt.get_width() / 2, 60))
        surface.blit(self.player_txt, (300 - self.player_txt.get_width() / 2, 40))
        surface.blit(self.attack_txt, (300 - (self.attack_txt.get_width() + self.inv_txt.get_width() +
                                              self.esc_txt.get_width()) / 2, 460))
        surface.blit(self.inv_txt, (300 - self.inv_txt.get_width() / 2, 460))
        surface.blit(self.esc_txt, (300 + self.inv_txt.get_width() / 2, 460))
        # Monster images display.
        for index, monster in enumerate(self.house.monsters):
            self.hp_text = self.font1.render("HP: " + "%.f" % monster.hp + "/" + str(monster.maxhp), True,
                                             (112, 89, 154))
            if index < 5:
                surface.blit(monster.monsterimg, ((index * 100) + 50, 130))
                surface.blit(self.hp_text, ((index * 100) + 50, 110))
            else:
                surface.blit(monster.monsterimg, (((index - 5) * 100) + 70, 300))
                surface.blit(self.hp_text, (((index - 5) * 100) + 70, 280))
