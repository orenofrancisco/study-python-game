import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        # Inherit properties from Sprite
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load the sprite
        self.image = pygame.image.load('../images/ship_grey.png').convert_alpha()
        self.rect = self.image.get_rect()

        # Spawn the aliens reasonably close to the origin
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's position as a float for smooth movement at low resolution
        self.x = float(self.rect.x)

    def blit_me(self):
        # This is used to render the sprite on the screen
        self.screen.blit(self.image, self.rect)
