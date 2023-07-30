import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from decoration import Decoration
import game_functions as gf

def run_game():
    """ Initialize game and create a screen object """
    pygame.init()
    settings = Settings()

    # Create a screen
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption(settings.window_caption)

    # Create player object
    ship = Ship(settings, screen)
    
    # A [Group] is a special list made inside pygame
    bullets = Group()

    # Instance the aliens and create a fleet of them
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    # Create group of decorations
    decorations = []
    gf.create_decorations(settings, screen, decorations)
    
    while True:
        # Check for events
        gf.check_events(settings, screen, ship, bullets)

        # Update game logic
        ship.update()
        gf.update_decorations(decorations, settings)
        gf.update_bullets(bullets)

        # Draw calls
        gf.update_screen(settings, screen, ship, aliens, bullets, decorations)

run_game()
