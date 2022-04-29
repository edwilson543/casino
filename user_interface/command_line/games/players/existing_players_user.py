from games.player_base_class import PlayerType
from user_interface.command_line.games.player_base_class_user import PlayerUser
from datetime import datetime
from enum import Enum

# TODO create a read/write mechanism that saves each game/ allows creation of new players
##########
# Instantiate the players
##########

Ed = PlayerUser(
    player_type=PlayerType.EXISTING_PLAYER,
    name='Ed',
    username='edwilson543',
    password='roulette1',
    initial_pot=100,
    initial_pot_datetime=datetime(2022, 4, 7),
    active_pot=5,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=None,
    active_session_start_time=None,
    active_session_top_ups=0,
    all_in_status=False)

Balint = PlayerUser(
    player_type=PlayerType.EXISTING_PLAYER,  # existing player
    name='Balint',
    username='balint1',
    password='roulette2',
    initial_pot=100,
    initial_pot_datetime=datetime(2022, 4, 7),
    active_pot=5,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=None,
    active_session_start_time=None,
    active_session_top_ups=0,
    all_in_status=False)

Guest = PlayerUser(
    player_type=PlayerType.EXISTING_PLAYER,  # guest player
    name='guest',
    username='guest',
    password='guest',
    initial_pot=0,
    initial_pot_datetime=datetime(2022, 4, 7),
    active_pot=0,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=None,
    active_session_start_time=None,
    active_session_top_ups=0,
    all_in_status=False)


#####################
# Add player to the list of available players
#####################
class ExistingPlayersUser(Enum):
    edwilson543 = Ed
    balint1 = Balint
    guest = Guest
