import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        # Inherit parent's attributes and methods
        super().__init__()
        self.screen = screen

        # Bullets spawn at the ship's location
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)

        # Then move it to the ship's position, specifically the nose of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

        # Copy the remaining settings here
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        # Move the bullet up
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
