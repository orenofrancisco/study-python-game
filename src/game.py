import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    """ Initialize game and create a screen object """
    pygame.init()
    game_settings = Settings()

    # Create a screen
    screen = pygame.display.set_mode(game_settings.screen_size)
    pygame.display.set_caption(game_settings.window_caption)

    # Create player object
    ship = Ship(game_settings, screen)
    
    # A [Group] is a special list made inside pygame
    bullets = Group()

    # Instance an alien
    alien = Alien(game_settings, screen)

    while True:
        # Check for events
        gf.check_events(game_settings, screen, ship, bullets)

        # Update game logic
        ship.update()
        gf.update_bullets(bullets)

        # Draw calls
        gf.update_screen(game_settings, screen, ship, alien, bullets)

run_game()
