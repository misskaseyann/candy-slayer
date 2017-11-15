import sys
import pygame
from candy_slayer.Game import Game

def run_game():
    # Initalize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((400, 360))
    pygame.display.set_caption("Candy Slayer")
    # Create the game.
    game = Game()

    # background
    background = (255, 241, 235)
    screen.fill(background)
    font = pygame.font.Font('freesans.ttf', 32)
    

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()