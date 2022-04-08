from Games.games_base_classes import Player
from datetime import datetime


####################
# Assign the players
####################

class Ed(Player):
    def __init__(self,
                 player_type='E',  # existing player
                 name: str = 'Ed',
                 username: str = 'edwilson543',
                 password: str = 'roulette1',
                 initial_pot: int = 100,
                 initial_pot_datetime: datetime = datetime(2022, 4, 7),
                 active_pot: int = 5,
                 last_top_up_datetime: datetime = None):
        super().__init__(player_type, name, username, password,
                         initial_pot, initial_pot_datetime, active_pot, last_top_up_datetime)


class Balint(Player):
    def __init__(self,
                 player_type='E',  # existing player
                 name: str = 'Balint',
                 username: str = 'balint1',
                 password: str = 'roulette2',
                 initial_pot: int = 100,
                 initial_pot_datetime: datetime = datetime(2022, 4, 7),
                 active_pot: int = 5,
                 last_top_up_datetime: datetime = None):
        super().__init__(player_type, name, username, password,
                         initial_pot, initial_pot_datetime, active_pot, last_top_up_datetime)


class Guest(Player):
    def __init__(self,
                 player_type='G',  # guest player
                 name: str = 'guest',
                 username: str = 'guest',
                 password: str = None,
                 initial_pot: int = 0,
                 initial_pot_datetime: datetime = datetime(2022, 4, 7),
                 active_pot: int = 0,
                 last_top_up_datetime: datetime = None):
        super().__init__(player_type, name, username, password,
                         initial_pot, initial_pot_datetime, active_pot, last_top_up_datetime)


#####################
# Add player to the list of available players
#####################
existing_players = {'edwilson543': Ed(), 'balint1': Balint(), 'guest': Guest()}
