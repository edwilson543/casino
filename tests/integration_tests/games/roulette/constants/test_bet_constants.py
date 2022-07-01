"""Module for unit tests on consistency of bet constants"""

# Standard library imports
from dataclasses import fields

 # Local application imports
from games.roulette.constants.bet_constants import BetTypeIds, InsideBetTypePrompts, OutsideBetTypePrompts, \
    WheelDefaultBetOptionsAndParameters
from games.roulette.definitions.bet_type_defns import BetTypeOptions

# Local application UI imports
from user_interface.games.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser


class TestBetConstantsConsistent:
    """
    Class to test whether all bets have been fully defined in the bet_constants module.
    In particular, whether the same list of bets exists in the front and backend, and whether all these
    bets have IDs and prompts.
    """

    # Test IDs are 1 to 1 with backend
    def test_all_backend_bet_objects_have_bet_ids(self):
        for bet in BetTypeOptions:
            bet_name = BetTypeOptions(bet).name
            assert hasattr(BetTypeIds, bet_name)

    def test_all_bets_with_ids_have_backend_bet_object(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(BetTypeOptions, bet_name)

    # Test IDs are 1 to 1 with frontend
    def test_all_frontend_bet_objects_have_bet_ids(self):
        for bet in BetTypeOptionsUser:
            bet_name = BetTypeOptionsUser(bet).name
            assert hasattr(BetTypeIds, bet_name)

    def test_all_bets_with_ids_have_frontend_bet_object(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(BetTypeOptionsUser, bet_name)

    # Test IDs are 1 to 1 with prompts (prompts as a union of inside and outside prompts)
    def test_all_bets_with_ids_have_corresponding_prompt(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(OutsideBetTypePrompts, bet_name) or hasattr(InsideBetTypePrompts, bet_name)

    def test_all_outside_bet_prompts_have_corresponding_ids(self):
        for bet_prompt in OutsideBetTypePrompts:
            bet_name = OutsideBetTypePrompts(bet_prompt).name
            assert hasattr(BetTypeIds, bet_name)

    def test_all_inside_bet_prompts_have_corresponding_ids(self):
        for bet_prompt in InsideBetTypePrompts:
            bet_name = InsideBetTypePrompts(bet_prompt).name
            assert hasattr(BetTypeIds, bet_name)

    # Test IDs are 1 to 1 with defined bet data class
    def test_all_bet_ids_have_corresponding_default_data(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(WheelDefaultBetOptionsAndParameters, bet_name)

    def test_all_bets_with_data_have_ids(self):
        for bet_type in fields(WheelDefaultBetOptionsAndParameters):
            assert hasattr(BetTypeIds, bet_type.name)
