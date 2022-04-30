from games.player_base_class import PlayerData, PlayerType
from datetime import datetime
from dataclasses import dataclass


ed_data = PlayerData(
    player_type=PlayerType.EXISTING_PLAYER,
    name='Ed',
    username='edwilson543',
    password='roulette1',
    active_pot=100,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=0,
    active_session_start_time=datetime.now(),
    active_session_top_ups=0)

balint_data = PlayerData(
    player_type=PlayerType.EXISTING_PLAYER,  # existing player
    name='Balint',
    username='balint1',
    password='roulette2',
    active_pot=100,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=0,
    active_session_start_time=datetime.now(),
    active_session_top_ups=0)

guest_data = PlayerData(
    player_type=PlayerType.GUEST_PLAYER,  # guest player
    name='guest',
    username='guest',
    password='guest',
    active_pot=0,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=0,
    active_session_start_time=datetime.now(),
    active_session_top_ups=0)

@dataclass
class AllPlayerData:
    edwilson543 = ed_data
    balint1 = balint_data
    guest = guest_data