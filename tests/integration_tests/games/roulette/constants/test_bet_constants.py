"""Tests whether all bets have been fully defined in the bet_constants module."""

from games.roulette.constants.bet_constants import BetTypeIds, InsideBetTypePrompts, OutsideBetTypePrompts, \
    WheelDefaultBetOptionsAndParameters
from games.roulette.definitions.bet_type_defns import BetTypeOptions
from user_interface.command_line.roulette.definitions.bet_type_defns_user import BetTypeOptionsUser
from dataclasses import fields


class TestBetConstantsConsistent:
    def test_all_backend_bet_objects_have_bet_ids(self):
        for bet_name, _ in BetTypeOptions.__members__.items():
            assert hasattr(BetTypeIds, bet_name)

    def test_all_bets_with_ids_have_backend_bet_object(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(BetTypeOptions, bet_name)

    def test_all_frontend_bet_objects_have_bet_ids(self):
        for bet_name, _ in BetTypeOptionsUser.__members__.items():
            assert hasattr(BetTypeIds, bet_name)
            assert hasattr(BetTypeIds, bet_name)

    def test_all_bets_with_ids_have_frontend_bet_object(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(BetTypeOptionsUser, bet_name)

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

    def test_all_bet_ids_have_corresponding_default_data(self):
        for bet_id in BetTypeIds:
            bet_name = BetTypeIds(bet_id).name
            assert hasattr(WheelDefaultBetOptionsAndParameters, bet_name)

    def test_all_bets_with_data_have_ids(self):
        for bet_type in fields(WheelDefaultBetOptionsAndParameters):
            assert hasattr(BetTypeIds, bet_type.name)
