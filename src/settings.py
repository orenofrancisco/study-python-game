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
        self.framerate_cap = 30

        # Ship related settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets = 8

        # Alien settings
        self.alien_drop_speed = 8
        self.speedup_scale = 1.3

        # Decoration settings
        self.decoration_max = 10
        self.decoration_spread = self.screen_height / self.decoration_max
        self.decoration_speed = 2
        self.decoration_frames_since_last_draw = 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # We can call this function to reset the progress the player has made
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 10
        self.alien_speed = 8
        self.alien_points = 50
        self.alien_direction = 1    # 1 = right, -1 left

    def increase_speed(self):
        # This function works as a sort of difficulty mechanism to make the game
        # more replayable. It speeds up the game a bit.
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
