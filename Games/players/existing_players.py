from Games.games_base_classes import Player
from datetime import datetime


####################
# Assign the players
####################

class Ed(Player):
    def __init__(self,
                 name: str = 'ed',
                 username: str = 'edwilson543',
                 password: str = 'roulette1',
                 initial_pot: int = 0,
                 initial_pot_datetime: datetime = datetime(2022, 4, 7),
                 active_pot: int = 0):
        super().__init__(name, username, password, initial_pot, initial_pot_datetime, active_pot)


class Balint(Player):
    def __init__(self,
                 name: str = 'balint',
                 username: str = 'balint1',
                 password: str = 'roulette2',
                 initial_pot: int = 0,
                 initial_pot_datetime: datetime = datetime(2022, 4, 7),
                 active_pot: int = 0):
        super().__init__(name, username, password, initial_pot, initial_pot_datetime, active_pot)


class Guest(Player):
    def __init__(self,
                 name: str = 'guest',
                 username: str = 'guest',
                 password: str = None,
                 initial_pot: int = 0,
                 initial_pot_datetime: datetime = datetime(2022, 4, 7),
                 active_pot: int = 0):
        super().__init__(name, username, password, initial_pot, initial_pot_datetime, active_pot)


#####################
# Add player to the list of available players
#####################
existing_players = {'edwilson543': Ed(), 'balint1': Balint()}
