class Settings():
    """ This class is to store configuration options that
    are used at program initialization. Instantiate this class
    once directly after [pygame.init()] and store all your settings here """

    def __init__(self):
        # Screen and window related settings
        self.screen_width = 800
        self.screen_height = 480
        self.screen_size = (self.screen_width, self.screen_height)
        self.window_caption = "Space Invaders"
        self.bg_color = (85, 205, 255)

        # Ship related settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 7.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets = 5

        # Decoration settings
        self.decoration_spread = 128
        self.decoration_speed = 0.5
        self.decoration_max = 6
