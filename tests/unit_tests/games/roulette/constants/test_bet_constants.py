from games.roulette.constants.bet_constants import WheelDefaultBetOptionsAndParameters, default_colours_bet_parameters, \
    default_straight_up_bet_parameters

test_wheel_parameters = WheelDefaultBetOptionsAndParameters(COLOURS_BET=default_colours_bet_parameters,
                                                            STRAIGHTUP_BET=default_straight_up_bet_parameters)


class TestIndividualWheelMinMaxBetParameters:
    def test_construct_wheel_bet_options_prompt(self):
        expected_prompt = "[C]-Colours, [S]-Straight Up, [P]-Split, [H] - High / Low, [O] - Odds / Evens"
        actual_prompt = test_wheel_parameters.construct_wheel_bet_options_prompt()
        assert expected_prompt == actual_prompt

