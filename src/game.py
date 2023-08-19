import sys
import pygame
from pygame.sprite import Group
from pygame.time import Clock

from settings import Settings
from ship import Ship
from alien import Alien
from decoration import Decoration
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
    """ Initialize game and create a screen object """
    pygame.init()
    settings = Settings()
    stats = GameStats(settings)

    # Create a clock to limit framerate
    # So far that's its only responsibility
    timer = Clock()

    # Create a screen
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption(settings.window_caption)

    # Big loud play button
    play_button = Button(settings, screen, "Play")

    # Create player object
    ship = Ship(settings, screen)
    
    # A [Group] is a special list made inside pygame
    # Groups have an update method prototype that we
    # are implementing on our class definitions, so when we call
    # thing.update() the entire group will call their own update()
    # method in the background.
    bullets = Group()

    # Instance the aliens and create a fleet of them
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)

    # Create group of decorations
    # TODO: Actually use a Group(), I used a basic list because I couldn't get
    # TODO: the group to work. 
    decorations = []
    gf.create_decorations(settings, screen, decorations)

    while True:
        # Check for events
        gf.check_events(settings, screen, stats, play_button, ship, aliens, bullets)

        # Update game logic, should only happen if the gamestate is 'active'
        if stats.game_active:
            ship.update()
            gf.update_decorations(decorations, settings)
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(screen, settings, ship, stats, aliens, bullets)

        # Draw calls
        gf.update_screen(settings, screen, stats, ship, aliens, bullets, decorations, play_button)

        # Delay for next frame
        timer.tick(settings.framerate_cap)

run_game()
