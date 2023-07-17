import sys
import pygame

def check_events():
    # Monitor for KB/M events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, ship):
    # Draw calls
    screen.fill(settings.bg_color)
    ship.blit_me()

    # Refresh screen
    pygame.display.flip()
