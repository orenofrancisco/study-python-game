import pygame.font

from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    # One of the few UI pieces in the game, it displays lives and score
    # for the current run.

    def __init__(self, settings, screen, stats):
        # Make local copies of the function arguments
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # Round the score to a multiple of 10
        rounded_score = int(round(self.stats.score, -1))
        
        # Generate the image of the text
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Now the bounding box it will live in
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        # Generate the texture for the high score
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        # Position the box for the score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        # Generate the texture for the high score
        self.level_str = str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True,
                self.text_color, self.settings.bg_color)

        # Position the box for the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        # Generate/update the sprites to be drawn
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + (ship_number * ship.rect.width)
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        # Draw the score on the screen
        self.screen.blit(self.score_image, self.score_rect)

    def show_high_score(self):
        # Draw high score on the screen
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def show_level(self):
        # Draw the current level on the screen
        self.screen.blit(self.level_image, self.level_rect)

    def show_ships(self):
        # Draw all the ships that represent the players' lives left
        self.ships.draw(self.screen)
