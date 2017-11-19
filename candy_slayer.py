import sys
import pygame

from Manager import Manager
from candy_slayer.Game import Game
from game_state.InventoryScreen import InventoryScreen
from game_state.NeighborhoodScreen import NeighborhoodScreen
from game_state.TitleScreen import TitleScreen

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 540))
    pygame.display.set_caption("Candy Slayer")
    manager = Manager()
    states = {"TITLE": TitleScreen(manager),
              "NEIGHBORHOOD": NeighborhoodScreen(manager),
              "INVENTORY": InventoryScreen(manager)}
    game = Game(screen, states, "TITLE")
    manager.add_game(game)
    game.run()
    pygame.quit()
    sys.exit()
