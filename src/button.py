import pygame.font

class Button():
    # This is a simple button that will comprise all of our UI
    # There is nothing else, just a button for now

    def __init__(self, settings, screen, message):
        # Copy some values locally first, we'll need them.
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define basic properties of the button in question
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Define the rect we'll use to move the thing later
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Initialize the button text
        self.prep_message(message)

    def prep_message(self, message):
        # Pygame Font text must rendered onto an image you can blit
        # This is how
        self.message_image = self.font.render(message, True, 
                self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        # Now to draw the text on the screen!
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
