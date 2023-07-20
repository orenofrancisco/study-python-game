import sys
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    # Monitor for KB/M events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen, ship, bullets)

def check_keydown_events(event, settings, screen, ship, bullets):
    # This function only handles activating the lateral movement of the ship
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        # Spawn a bullet and add it to the list
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, settings, screen, ship, bullets):
    # This function only handles deactivating the lateral movement of the ship
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets):
    # Draw calls
    screen.fill(settings.bg_color)
    ship.blit_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Refresh screen
    pygame.display.flip()
