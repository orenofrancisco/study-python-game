import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """ Initialize game and create a screen object """
    pygame.init()
    game_settings = Settings()

    # Create a screen
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption(game_settings.window_caption)

    # Create player object
    ship = Ship(screen)

    while True:
        # Check for events
        gf.check_events()

        # Draw calls
        gf.update_screen(game_settings, screen, ship)

run_game()
