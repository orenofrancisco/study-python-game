class GameStats():
    # This class is meant to store information about game state.
    # While the Settings class holds information about the initial state of
    # the game, this one will hold information about the current state.
    # Track victory/loss conditions here, as well as score and other
    # stateful information (buffs, debuffs, or other temporary things)

    def __init__(self, settings):
        self.settings = settings
        self.high_score = 0
        self.reset_stats()

        # Start the game in 'active' state
        # Loss conditions will later set this to false and the game ends.
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
