"""Integration tests for the player_database_manager"""

from games.players.player_database_manager import PlayerDatabaseManager
from games.players.player_base_class import Player
from games.all_game_constants.root_directory import ROOT_DIRECTORY
from datetime import datetime
import pytest


class TestPlayerDatabaseManagerIntegration:
    """Class for testing various combinations of uploading, downloading, editing players etc."""

    @pytest.fixture(scope="class")
    def test_player_database_manager(self):
        return PlayerDatabaseManager(
            player_object=Player,
            player_data_directory_path=ROOT_DIRECTORY / "tests" / "test_data" / "player_data",
            player_datafile_name="test_player_data.json",
            guest_datafile_name="test_guest_data.json")

    @pytest.fixture(scope="class")
    def test_player_three(self):
        return Player(
            name="Test Three", username="test_three", password="test_3", active_pot=1000, total_active_stake=0,
            last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
            active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
            active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))

    def test_create_then_delete_player(self, test_player_database_manager):
        """Integration test to test whether creating and deleting a dummy new player works as expected."""
        test_player_database_manager.create_player(name="Test Four", player_username="test_four", password="test4")
        assert test_player_database_manager.username_exists_check(player_username="test_four")
        test_player_database_manager.delete_player(player_username="test_four")
        assert not test_player_database_manager.username_exists_check(player_username="test_four")

    def test_upload_load_player_then_delete_player(self, test_player_database_manager, test_player_three):
        """
        Integration test to test whether uploading and then downloading a player works (and also then deleting that
        player so that the test can be repeated with the same set up).
        """
        test_player_database_manager.upload_player(player=test_player_three)
        assert test_player_database_manager.username_exists_check(player_username="test_three")
        loaded_test_player_three = test_player_database_manager.load_player(player_username="test_three")
        assert loaded_test_player_three == test_player_three
        test_player_database_manager.delete_player(player_username="test_three")
        assert not test_player_database_manager.username_exists_check(player_username="test_three")

    def test_load_player_change_them_upload_load_check_parameters_saved(self, test_player_database_manager,
                                                                        test_player_three):
        """
        Integration test to check that a player can be loaded, played with (and therefore their parameters changed)
        and then uploaded and downloaded, and the changed parameters will have been saved.
        This reflects what will happen it actual game play.
        Note we upload a dummy player first.
        """
        test_player_database_manager.upload_player(player=test_player_three)
        new_test_player_three = test_player_database_manager.load_player(player_username="test_three")
        new_test_player_three.add_winnings_to_pot(amount=100)
        new_test_player_three.take_stake_from_pot(amount=90)
        test_player_database_manager.upload_player(player=new_test_player_three)
        updated_test_player_three = test_player_database_manager.load_player(player_username="test_three")
        assert updated_test_player_three.active_pot == 1010  # 1000 + 100 - 90
        test_player_database_manager.delete_player(player_username="test_three")
