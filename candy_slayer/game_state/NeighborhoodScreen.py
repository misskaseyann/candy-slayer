import os
import pygame

from candy_slayer.game_state.GameState import GameState


class NeighborhoodScreen(GameState):
    """
    Neighborhood game state object.

    Music credit: Visager @ https://soundcloud.com/visagermusic
    Font credit: Alagard @ https://www.dafont.com/alagard.font
    """
    def __init__(self, manager):
        """
        Initialize the neighborhood game state.

        :param manager: game object manager
        """
        super().__init__(manager)
        self.neighborhoodx = self.manager.neighborhood.get_width()
        self.neighborhoody = self.manager.neighborhood.get_height()
        self.playerx = (335 - ((self.neighborhoodx * 100) / 2))
        self.playery = (300 - ((self.neighborhoody * 80) / 2))
        self.housex = 0
        self.housey = 0

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        :param persistent: a dict passed from state to state
        """
        pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "eerieloop.wav"))
        pygame.mixer.music.play(-1)
        self.font = pygame.font.Font(os.path.join("candy_slayer/assets/", "alagard.ttf"), 16)
        self.house_img = pygame.image.load(os.path.join("candy_slayer/assets/", "house.png")).convert_alpha()
        self.player_img = pygame.image.load(os.path.join("candy_slayer/assets/", "player.png")).convert_alpha()
        self.enemies_txt = self.font.render("Monsters: " + str(self.manager.get_population()) + "  |  Health: " +
                                            str(self.manager.get_player().get_currhp()) + "/" +
                                            str(self.manager.get_player().get_hpmax()) + "  |  Weapon: " +
                                            str(self.manager.get_player().get_currweapon().get_name()),
                                            True, (112, 89, 154))

    def get_event(self, event):
        """
        Handles events in the game.

        :param event: event to be handled
        """
        # If player exits, end the game.
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            # 'd' key moving the player to the right.
            if event.key == pygame.K_d:
                if self.playerx < (((self.neighborhoodx - 1) * 100) + (320 - ((self.neighborhoodx * 100)/2))):
                    self.housex += 1
                    self.playerx += 100
            # 'a' key moving the player to the left.
            if event.key == pygame.K_a:
                if self.playerx > (320 - (((self.neighborhoodx - 1) * 100)/2)):
                    self.housex -= 1
                    self.playerx -= 100
            # 'w' key moving the player up.
            if event.key == pygame.K_w:
                if self.playery > (280 - (((self.neighborhoody - 1) * 80)/2)):
                    self.housey -= 1
                    self.playery -= 80
            # 's' key moving the player down.
            if event.key == pygame.K_s:
                if self.playery < (((self.neighborhoody - 1) * 80) + (280 - ((self.neighborhoody * 80)/2))):
                    self.housey += 1
                    self.playery += 80
            # Enter button selects the house the player is entering.
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.load(os.path.join("candy_slayer/assets/", "battle.wav"))
                pygame.mixer.music.play(-1)
                self.manager.get_player().set_currhouse(
                    self.manager.get_neighborhood().get_house(self.housey, self.housex))
                self.next_state = "BATTLE"
                self.done = True

    def draw(self, surface):
        """
        Draw game objects on the screen.

        :param surface: game screen to be drawn on
        """
        surface.fill((255, 241, 235))
        for h in range(0, self.neighborhoody):
            for w in range(0, self.neighborhoodx):
                surface.blit(pygame.transform.scale(self.house_img, (64, 64)),
                             ((w * 100) + (320 - ((self.neighborhoodx * 100)/2)),
                              (h * 80) + (280 - ((self.neighborhoody * 80)/2))))
        surface.blit(self.player_img, (self.playerx, self.playery))
        surface.blit(self.enemies_txt, (300 - self.enemies_txt.get_width() / 2, 10))
