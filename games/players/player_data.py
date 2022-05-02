from games.player_base_class import PlayerData, PlayerType
from datetime import datetime
from dataclasses import dataclass

ed_data = PlayerData(
    player_type=PlayerType.EXISTING_PLAYER,
    name='Ed',
    username='edwilson543',
    password='roulette1',
    active_pot=100,
    total_active_stake=0,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=0,
    active_session_start_time=datetime.now(),
    active_session_top_ups=0,
    last_session_end_time=datetime(year=2022, month=5, day=2, hour=8, minute=23))

balint_data = PlayerData(
    player_type=PlayerType.EXISTING_PLAYER,  # existing player
    name='Balint',
    username='balint1',
    password='roulette2',
    active_pot=100,
    total_active_stake=0,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=0,
    active_session_start_time=datetime.now(),
    active_session_top_ups=0,
    last_session_end_time=datetime(2022, 5, 1))

guest_data = PlayerData(
    player_type=PlayerType.GUEST_PLAYER,  # guest player
    name='guest',
    username='guest',
    password='guest',
    active_pot=0,
    total_active_stake=0,
    last_top_up_datetime=datetime(2022, 4, 7),
    active_session_initial_pot=0,
    active_session_start_time=datetime.now(),
    active_session_top_ups=0,
    last_session_end_time=datetime.now())  # Note this never gets called


@dataclass
class AllPlayerData:
    edwilson543 = ed_data
    balint1 = balint_data
    guest = guest_data
