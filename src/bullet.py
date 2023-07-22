import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        # Inherit parent's attributes and methods
        super().__init__()
        self.screen = screen

        # Bullets spawn at the origin (0, 0)
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)

        # Then move it to the ship's position, specifically the nose of the ship
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # Store the bullet's position as a float
        self.x = float(self.rect.x)

        # Copy the remaining settings here
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        # Move the bullet to the right edge
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        # Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
