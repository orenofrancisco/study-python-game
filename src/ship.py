import pygame

class Ship():
    """ This class holds information relative to the player object, the ship.
    It has methods to draw it, and its constructor fetches information 
    from pygame to give it context-appropriate attributes. """

    def __init__(self, settings, screen):
        # During initialization, the ship should reference which screen
        # it should be drawn on, and collect some stats about it
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        # Get the ship picture and store statistics about it
        self.color = 'red'    # ok for green, blue, red or yellow
        self.image = pygame.image.load("../images/ship_" + self.color + ".png").convert_alpha()
        self.rect = self.image.get_rect()

        # The ship should spawn in the middle of the screen, left edge
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a float for the center to make it smooth
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
    
    def blit_me(self):
        # blit(what, where)
        self.screen.blit(self.image, self.rect)

    def update(self):
        # This method relies on the movement flags set up during init()
        if self.moving_up and self.rect.top > 0:
            self.center -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.settings.ship_speed_factor

        # Update coordinates
        self.rect.centery = self.center
