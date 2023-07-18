class Settings():
    """ This class is to store configuration options that
    are used at program initialization. Instantiate this class
    once directly after [pygame.init()] and store all your settings here """

    def __init__(self):
        # Screen and window related settings
        self.screen_size = (800,600)
        self.window_caption = "Space Invaders"
        self.bg_color = (85, 205, 255)

        # Ship related settings
        self.ship_speed_factor = 1.5
