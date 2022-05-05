"""Unit tests for the player_database_manager"""

from games.players.player_database_manager import PlayerDatabaseManager
from games.player_base_class import Player
from root_directory import ROOT_DIRECTORY
from datetime import datetime
import json
import pytest

test_player_database_manager = PlayerDatabaseManager(
    player_object=Player,
    player_data_directory_path=ROOT_DIRECTORY / "tests" / "test_data" / "player_data",
    player_datafile_name="test_player_data.json",
    guest_datafile_name="test_guest_data.json")

database_manager_alt_path = PlayerDatabaseManager(  # For testing cases where no file exists yet
    player_object=Player,
    player_data_directory_path=ROOT_DIRECTORY / "tests" / "test_data" / "player_data",
    player_datafile_name="test_player_data_non_existent.json",  # By default no file with this name exists
    guest_datafile_name="test_guest_data.json")

test_player_three = Player(
    name="Test Three", username="test_three", password="test_3", active_pot=1000, total_active_stake=0,
    last_top_up_datetime=datetime(2022, 4, 7, 2, 1),
    active_session_initial_pot=1000, active_session_start_time=datetime(2022, 5, 1, 3, 4),
    active_session_top_ups=0, last_session_end_time=datetime(2022, 4, 7, 2, 1))


class TestEncodeDecode:
    def test_encoded_then_decoded_player_unchanged(self):
        encoded_player = test_player_database_manager.encode_player(player=test_player_three)
        decoded_player = test_player_database_manager.decode_player(serialised_attributes_dict=encoded_player)
        assert test_player_three == decoded_player

    def test_encoded_then_decoded_player_unchanged_with_json(self):
        encoded_player_json = json.dumps(test_player_three, default=test_player_database_manager.encode_player)
        decoded_player = json.loads(encoded_player_json, object_hook=test_player_database_manager.decode_player)
        assert test_player_three == decoded_player


class TestPlayerStorage:
    ##########
    # load_player method unit tests
    # Note most methods can only be automatically tested by integration
    ##########
    def test_load_player_returns_specified_type_ordinary_player(self):
        loaded_player = test_player_database_manager.load_player(player_username="test_one")
        assert type(loaded_player) is Player

    def test_load_player_returns_test_one_player(self):
        loaded_player = test_player_database_manager.load_player(player_username="test_one")
        assert loaded_player.name == "Test One"
        assert loaded_player.username == "test_one"
        assert loaded_player.password == "test_one23"

    def test_load_player_raises_key_error_non_existent_player(self):
        with pytest.raises(KeyError):
            test_player_database_manager.load_player(player_username="i_dont_exist")

    def test_load_player_returns_specified_type_guest_player(self):
        loaded_player = test_player_database_manager.load_player(player_username="guest")
        assert type(loaded_player) is Player

    def test_load_player_returns_guest_player(self):
        loaded_player = test_player_database_manager.load_player(player_username="guest")
        assert loaded_player.name == "As a guest"
        assert loaded_player.username == "guest"
        assert loaded_player.password == "guest123"

    def test_delete_player_that_does_not_exist(self):
        """
        Test to check that the delete_player method raises an error if asked to
        deleted a player who does not exist.
        """
        with pytest.raises(ValueError):
            test_player_database_manager.delete_player(player_username="i_dont_exist")
    ##########
    # create_player_data_file unit tests
    ##########

    def test_create_player_data_file_does_not_exist_yet(self):
        database_manager_alt_path.create_player_data_file()
        new_player_data_path = ROOT_DIRECTORY / "tests" / "test_data" / "player_data" / "test_player_data_non_existent.json"
        assert new_player_data_path.is_file()
        new_player_data_path.unlink()  # Deletes the new file so that the test can be re-run

    def test_create_player_data_file_raises_error_existing_player_data(self):
        with pytest.raises(FileExistsError):
            test_player_database_manager.create_player_data_file()
    ##########
    # get_data_path unit tests
    ##########

    def test_get_data_path_player_data_file_does_not_exist_yet(self):
        actual_path = database_manager_alt_path.get_data_path(player_username="witch")
        expected_path = ROOT_DIRECTORY / "tests" / "test_data" / "player_data" / "test_player_data_non_existent.json"
        assert actual_path == expected_path
        expected_path.unlink()  # Deletes the new file so that the test can be re-run

    def test_get_data_path_guest_player(self):
        expected_path = ROOT_DIRECTORY / "tests" / "test_data" / "player_data" / "test_guest_data.json"
        actual_path = test_player_database_manager.get_data_path(player_username="guest")
        assert expected_path == actual_path

    def test_get_data_path_existing_user_player(self):
        expected_path = ROOT_DIRECTORY / "tests" / "test_data" / "player_data" / "test_player_data.json"
        actual_path = test_player_database_manager.get_data_path(player_username="test_one")
        assert expected_path == actual_path

    ##########
    # Unit test on lower level username methods
    ##########

    #  Username existence checks
    def test_username_existence_check_existing_player(self):
        user_exists = test_player_database_manager.username_exists_check(player_username="test_one")
        assert user_exists

    def test_username_existence_check_non_existing_player(self):
        user_exists = test_player_database_manager.username_exists_check(player_username="i_dont_exist")
        assert not user_exists

    #  Username criteria checks
    def test_username_meets_criteria_check_valid_username(self):
        valid_username = "witch"
        username_passed = test_player_database_manager.username_meets_criteria_check(proposed_username=valid_username)
        assert username_passed

    def test_username_meets_criteria_check_invalid_username(self):
        invalid_username = "witch !"
        username_passed = test_player_database_manager.username_meets_criteria_check(proposed_username=invalid_username)
        assert not username_passed

    #  Password criteria checks
    def test_password_meets_criteria_check_valid_password(self):
        valid_password = "witchy"
        password_passed = test_player_database_manager.password_meets_criteria_check(proposed_password=valid_password)
        assert password_passed

    def test_password_meets_criteria_check_invalid_password(self):
        invalid_password = "wich"  # as length < 5
        password_passed = test_player_database_manager.password_meets_criteria_check(proposed_password=invalid_password)
        assert not password_passed

    #  Name criteria checks
    def test_name_meets_criteria_check_valid_name(self):
        valid_name = "Wesley"
        name_passed = test_player_database_manager.name_meets_criteria_check(proposed_name=valid_name)
        assert name_passed

    def test_name_meets_criteria_check_invalid_name(self):
        invalid_name = "Wesley!!!!!!!!!"
        name_passed = test_player_database_manager.name_meets_criteria_check(proposed_name=invalid_name)
        assert not name_passed
