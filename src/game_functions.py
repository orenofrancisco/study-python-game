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
    # This function only handles activating the vertical movement of the ship
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def check_keyup_events(event, settings, screen, ship, bullets):
    # This function only handles deactivating the vertical movement of the ship
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def update_screen(settings, screen, ship, bullets):
    # Draw calls
    screen.fill(settings.bg_color)
    ship.blit_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Refresh screen
    pygame.display.flip()

def update_bullets(bullets, screen):
    # Housekeeping of bullets and logic update of the objects
    bullets.update()

    # Remove bullets that are above drawing distance
    for bullet in bullets.copy():
        if bullet.rect.left >= 800: # TODO: Change hardcoded value for screen's value
            bullets.remove(bullet)

def fire_bullet(settings, screen, ship, bullets):
    # Spawn a bullet and add it to the list
    if len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

