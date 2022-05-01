from games.roulette.constants.bet_constants import WheelDefaultBetOptionsAndParameters, default_colours_bet, \
    default_straight_up_bet

test_wheel_parameters = WheelDefaultBetOptionsAndParameters(COLOURS_BET=default_colours_bet,
                                                            STRAIGHTUP_BET=default_straight_up_bet)


class TestIndividualWheelMinMaxBetParameters:
    def test_construct_wheel_bet_options_prompt(self):
        expected_prompt = "[C]olours, [S]traight up"
        actual_prompt = test_wheel_parameters.construct_wheel_bet_options_prompt()
        assert expected_prompt == actual_prompt

