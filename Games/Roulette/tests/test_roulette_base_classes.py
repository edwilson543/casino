from Games.Roulette.definitions.wheel_defns import wheel_options

euro_wheel = wheel_options['E']


# TODO write more tests - also find out how to write tests which navigate the game, rather than having to play it
# probably one to wait until more of a finished article

class TestRouletteWheel:
    def test_wheel_size_euro_wheel(self):
        assert euro_wheel.wheel_size() == 37

    def test_wheel_colour_counts_red(self):
        assert euro_wheel.colour_counts(colour='red') == 18

    def test_user_colour_options(self):
        assert euro_wheel.user_colour_options() == "[B]lack, [G]reen, [R]ed"

    def test_generate_colour_ids(self):
        assert euro_wheel.generate_colour_ids() == {'B': 'black', 'G': 'green', 'R': 'red'}

    def test_user_number_list(self):
        assert euro_wheel.user_number_list() == "[0, 36] (inclusive)"
