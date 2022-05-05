from games.player_base_class import Player
from datetime import datetime

test_player_one = Player(name="test", username="test", password="tst123", active_pot=1000, total_active_stake=0,
                         last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
                         active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                         active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

test_player_one_copy = Player(name="test", username="test", password="tst123", active_pot=1000, total_active_stake=0,
                              last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
                              active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                              active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

test_player_two = Player(name="test_two", username="test_two", password="tst131", active_pot=100, total_active_stake=0,
                         last_top_up_datetime=datetime(2022, 3, 7, 2, 1),
                         active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                         active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))


class TestPlayer:
    def test_player_equivalence_true(self):
        assert test_player_one == test_player_one_copy

    def test_player_equivalence_false(self):
        assert test_player_one != test_player_two
