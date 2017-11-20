import sys
import pygame

from candy_slayer.Manager import Manager
from candy_slayer.Game import Game
from candy_slayer.game_state.BattleScreen import BattleScreen
from candy_slayer.game_state.GameOverScreen import GameOverScreen
from candy_slayer.game_state.InventoryScreen import InventoryScreen
from candy_slayer.game_state.NeighborhoodScreen import NeighborhoodScreen
from candy_slayer.game_state.TitleScreen import TitleScreen
from candy_slayer.game_state.WinningScreen import WinningScreen

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 540))
    pygame.display.set_caption("Candy Slayer")
    manager = Manager()
    states = {"TITLE": TitleScreen(manager),
              "NEIGHBORHOOD": NeighborhoodScreen(manager),
              "INVENTORY": InventoryScreen(manager),
              "BATTLE": BattleScreen(manager),
              "GAMEOVER": GameOverScreen(manager),
              "WINNER": WinningScreen(manager)}
    game = Game(screen, states, "TITLE")
    manager.add_game(game)
    game.run()
    pygame.quit()
    sys.exit()
