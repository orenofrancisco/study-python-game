import pygame

class Decoration():
    # This is a class designed to draw background sprites
    # intended for decoration, such as stars, clouds or such things.
    # The logic is designed to be visual only, there are currently no
    # plans to include collission or interactivity with any other module

    def __init__(self, settings, screen):
        # For this object, we need an image of a cloud
        self.image = pygame.image.load("../images/cloud.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Copy settings from initializator arguments
        self.settings = settings
        self.screen = screen
    
    def blit_me(self):
        # This is used to render the sprite on the screen
        # Lifted from alien.py
        self.screen.blit(self.image, self.rect)
