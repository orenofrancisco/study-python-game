import pygame.font

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

    def prep_score(self):
        # First generate the image of the text
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Now the bounding box it will live in
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        # Draw the score on the screen
        self.screen.blit(self.score_image, self.score_rect)
