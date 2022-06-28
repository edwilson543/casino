from games.players.player_base_class import Player
from datetime import datetime
import pytest


class TestPlayer:
    """Class for conducting unit tests on Player base class"""

    @pytest.fixture(scope="class")
    def test_player_one(self):
        return Player(name="test", username="test", password="tst123", active_pot=1000, total_active_stake=0,
                      last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
                      active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                      active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

    @pytest.fixture(scope="class")
    def test_player_one_copy(self):
        return Player(name="test", username="test", password="tst123", active_pot=1000, total_active_stake=0,
                      last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
                      active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                      active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

    @pytest.fixture(scope="class")
    def test_player_two(self):
        return Player(name="test_two", username="test_two", password="tst131", active_pot=100, total_active_stake=0,
                      last_top_up_datetime=datetime(2022, 3, 7, 2, 1),
                      active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
                      active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

    def test_player_equivalence_true(self, test_player_one, test_player_one_copy):
        assert test_player_one == test_player_one_copy

    def test_player_equivalence_false(self, test_player_one, test_player_two):
        assert test_player_one != test_player_two
