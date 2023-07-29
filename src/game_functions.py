import sys
import pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(settings, screen, ship, bullets)
    if event.key == pygame.K_q: # Case insensitive, this procs for [q] and [Q]
        sys.exit()

def check_keyup_events(event, settings, screen, ship, bullets):
    # This function only handles deactivating the lateral movement of the ship
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, aliens, bullets):
    # Draw calls
    screen.fill(settings.bg_color)

    ship.blit_me()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Refresh screen
    pygame.display.flip()

def update_bullets(bullets):
    # Housekeeping of bullets and logic update of the objects
    bullets.update()

    # Remove bullets that are above drawing distance
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(settings, screen, ship, bullets):
    # Spawn a bullet and add it to the list
    if len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(settings, alien_width):
    # Function added to perform step [1] of create_fleet
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return available_space_x

def get_number_rows(settings, ship_height, alien_height):
    # Function added to perform step [2]
    available_space_y = (settings.screen_height - (3 * alien_height)
                        - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(settings, screen, aliens, x_index, y_index):
    # Function to be run [n] times during step [3] of create_fleet
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * x_index)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * y_index)
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    # This function has 3 steps:
    #   1 - Determine how many aliens fit laterally and create a 'row' of aliens
    #   2 - Determine how many aliens fit vertically and call that [n]
    #   3 - Run step [1], [n] times

    alien = Alien(settings, screen)
    number_aliens_per_row = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    # Create row of aliens
    for y_index in range(number_rows):
        for x_index in range(number_aliens_per_row):
            create_alien(settings, screen, aliens, x_index, y_index)
