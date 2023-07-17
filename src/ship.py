import pygame

class Ship():
    """ This class holds information relative to the player object, the ship.
    It has methods to draw it, and its constructor fetches information 
    from pygame to give it context-appropriate attributes. """

    def __init__(self, screen):
        # During initialization, the ship should reference which screen
        # it should be drawn on, and collect some stats about it
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Get the ship picture and store statistics about it
        self.image = pygame.image.load('../images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()

        # The ship should spawn in the middle of the screen, bottom row
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blit_me(self):
        # blit(what, where)
        self.screen.blit(self.image, self.rect)
