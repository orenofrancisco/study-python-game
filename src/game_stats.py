class GameStats():
    # This class is meant to store information about game state.
    # While the Settings class holds information about the initial state of
    # the game, this one will hold information about the current state.
    # Track victory/loss conditions here, as well as score and other
    # stateful information (buffs, debuffs, or other temporary things)

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        
