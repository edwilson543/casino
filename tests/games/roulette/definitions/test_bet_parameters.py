from games.roulette.definitions.bet_parameters import IndividualWheelMinMaxBetParameters, default_colours_bet, \
    default_straight_up_bet

test_wheel_parameters = IndividualWheelMinMaxBetParameters(COLOURS_BET=default_colours_bet,
                                                           STRAIGHTUP_BET=default_straight_up_bet)


class TestIndividualWheelMinMaxBetParameters:
    def test_construct_wheel_bet_options_prompt(self):
        expected_prompt = "[C]olours, [S]traight up"
        actual_prompt = test_wheel_parameters.construct_wheel_bet_options_prompt()
        assert expected_prompt == actual_prompt

    def test_get_wheel_bet_type_ids(self):
        expected_set = {"C", "S"}  # Note that order is not important here
        actual_list = test_wheel_parameters.get_wheel_bet_type_ids()
        actual_set = set(actual_list)
        assert expected_set == actual_set

