import sys
import pygame
from random import randint
from bullet import Bullet
from alien import Alien
from decoration import Decoration

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

def update_screen(settings, screen, ship, aliens, bullets, decorations):
    # Draw calls
    screen.fill(settings.bg_color)

    # Clouds go first
    for item in decorations:
        item.blit_me()

    # Then go dynamic objects
    ship.blit_me()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Refresh screen
    pygame.display.flip()

def update_bullets(aliens, bullets):
    # Housekeeping of bullets and logic update of the objects
    bullets.update()

    # Remove bullets that are above drawing distance
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # Check for collission with aliens and delete the pairs that touch
    # TODO: Why capture the return value? Are you doing something with it?
    collision = pygame.sprite.groupcollide(aliens, bullets, True, True)

def update_aliens(settings, aliens):
    # This group contains a basic update() call and will later host
    # the despawn calls in case of a hit, collission checks, and such
    check_fleet_edges(settings, aliens)
    aliens.update()

def fire_bullet(settings, screen, ship, bullets):
    # Spawn a bullet and add it to the list
    if len(bullets) < settings.max_bullets:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(settings, alien_width):
    # Function added to perform step [1] of create_fleet
    available_space_x = settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    # Function added to perform step [2] of create_fleet
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

def check_fleet_edges(settings, aliens):
    # If any aliens reach the edge, reverse direction and issue a drop order
    explored_aliens = 0
    for alien in aliens:
        if alien.check_edges():
            #print("Alien [" + str(explored_aliens) + "] found breaking bounds.")
            #print("\t[X: " + str(alien.rect.x) + "; Y: " + str(alien.rect.y)
            #        + "; W: " + str(alien.rect.w) + "; H: " + str(alien.rect.h) + "]")
            change_fleet_direction(settings, aliens)
            break
        else:
            explored_aliens += 1

def change_fleet_direction(settings, aliens):
    # This method issues the drop order on all aliens, and reverses the direction
    # they are going in
    for alien in aliens:
        alien.rect.y += settings.alien_drop_speed
    settings.alien_direction *= -1

def create_decorations(settings, screen, decorations):
    # Create a starting set of decorations to draw on screen
    for index in range(0, settings.decoration_max):
        rand_x = randint(0, settings.screen_width)
        new_decoration = Decoration(settings, screen)

        new_decoration.rect.x = rand_x
        new_decoration.rect.y = index * settings.decoration_spread

        decorations.append(new_decoration)

def cull_decorations(decorations, settings):
    # Function designed to cover step 1 of update_decorations
    for decoration in decorations.copy():
        if decoration.rect.top > settings.screen_height:
            decorations.remove(decoration)

def populate_decorations(decorations, settings):
    # Function designed to cover step 2 of update_decorations
    # First we need to determine if a new decoration is needed
    for item in decorations:
        sample = item
    
    settings.decoration_frames_since_last_draw += 1
    
    # This equation asks the question "Is there room for another decor?"
    if (settings.decoration_frames_since_last_draw > settings.decoration_spread
        and len(decorations) < settings.decoration_max):
        # The following logic is used in create_decorations as well
        new_decoration = Decoration(sample.settings, sample.screen)
        rand_x = randint(0, new_decoration.settings.screen_width)

        new_decoration.rect.x = rand_x
        new_decoration.rect.y = (-1 * new_decoration.rect.height)

        decorations.append(new_decoration)
        settings.decoration_frames_since_last_draw = 0

def update_decorations(decorations, settings):
    # Here we need to:
    #   A) Cull decorations that have gone beyond drawing distance
    #   B) Add new ones if we are below decoration_max and beyond the spread
    #   C) Move the existing ones
    # Not necessarily in that order
    for item in decorations:
        item.update()
    cull_decorations(decorations, settings)
    populate_decorations(decorations, settings)

# Timer stuff

