import sys
import pygame
import os
from candy_slayer.Game import Game

def run_game():
    # Initalize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((600, 540))
    pygame.display.set_caption("Candy Slayer")
    bg = pygame.image.load(os.path.join("candy_slayer/assets", "title.png")).convert()
    bg = pygame.transform.scale(bg, (600, 540))
    screen.blit(bg, (0, 0))

    # Create the game.
    game = Game()

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()