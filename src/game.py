import sys
import pygame
from settings import Settings
from ship import Ship

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
        # Monitor for KB/M events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw calls
        screen.fill(game_settings.bg_color)
        ship.blit_me()

        # Refresh screen
        pygame.display.flip()

run_game()
