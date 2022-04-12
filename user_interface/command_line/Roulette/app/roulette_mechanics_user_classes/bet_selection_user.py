from Games.games_base_classes import Player
from Games.Roulette.app.roulette_bet_base_class import RouletteBet
from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from user_interface.command_line.Roulette.definitions.wheel_defns_user import wheel_options_text
from Games.Roulette.definitions.bet_type_defns import bet_cats_and_types, bet_cat_options_text
from Games.Roulette.definitions.bet_type_defns import bet_type_options_text, bet_type_min_max_bet
from Games.Roulette.app.roulette_mechanics_action_classes.bet_selection import WheelAndBetTypeSelector
import sys


# TODO make this a subclass of WheelAndBetSelector
# TODO write down the empty methods below (bringing in wheel method)
# TODO do something with the stake method too, bring the high level call up to the top

class WheelAndBetTypeSelectorUser(WheelAndBetTypeSelector):
    """class to allow users to select the type of bet to place
    note note yet to place the bet"""

    def __init__(self,
                 wheel_look_up: dict,
                 bet_type_look_up: dict,
                 active_player: Player):
        super().__init__(wheel_look_up, bet_type_look_up)
        self.active_player = active_player

    def choose_playing_wheel(self) -> (str, RouletteWheel):
        """
        Method to navigate the user through the wheel options and return a live wheel object.
        Returns: the wheel_id, and the associated relevant subclass of RouletteWheel defining that wheel
        """
        while True:
            wheel_choice = input("What wheel would you like to play on?\n"
                                 f"{wheel_options_text}\n--->").upper()  # upper to allow for lower case
            if wheel_choice in list(self.wheel_look_up):
                return wheel_choice, self.get_wheel_from_wheel_id(wheel_choice)
            else:
                print("Invalid wheel choice, please try again")

    def choose_bet(self, wheel_id: str) -> RouletteBet:
        """
        Method that navigates the user to choose their bet, by applying the choose_playing_wheel,
        choose_bet_category and then the choose_bet_type methods below.
        """
        bet_cat = self.choose_bet_category(wheel_id=wheel_id)
        bet_type = self.choose_bet_type(wheel_id=wheel_id, bet_cat=bet_cat)
        return bet_type

    # Lower level methods called during the choose_bet method
    @staticmethod
    def choose_bet_category(wheel_id: str) -> str:
        while True:
            bet_cat = input("What category of bet would you like to place?"
                            f"\n{bet_cat_options_text[wheel_id]}\n--->").upper()
            if bet_cat in list(bet_cats_and_types[wheel_id].keys()):
                return bet_cat
            else:
                print("Not a valid bet category, try again")

    def choose_bet_type(self, wheel_id: str, bet_cat: str) -> RouletteBet:
        while True:
            bet_type_id = input("What category of bet would you like to place?"
                             f"\n{bet_type_options_text[wheel_id][bet_cat]}\n--->").upper()
            if bet_type_id in bet_cats_and_types[wheel_id][bet_cat]:
                return self.get_bet_type_from_bet_type_id(bet_type_id)
            else:
                print("Not a valid bet type, try again")

    def choose_stake_amount(self, bet_type):
        """Returns: Stake amount, all_in_status"""
        min_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['min']
        if self.player_funds < min_stake:  # TODO Add some feature here to allow user to do a top up instead
            all_in_stake, all_in_status = self.all_in()
            return all_in_stake, all_in_status
        else:
            all_in_stake, all_in_status = self.choose_stake_amount_funds_exceed_min_bet(bet_type=bet_type)
            return all_in_stake, all_in_status

    def choose_stake_amount_funds_exceed_min_bet(self, bet_type):
        """
        Returns:
        Stake amount, all_in_status, which by default is set to false
        """
        min_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['min']
        max_stake = bet_type_min_max_bet[self.wheel_id][bet_type]['max']
        all_in_status = False
        while True:
            stake = input("How much would you like to stake?\n"
                          f"Minimum stake: £{min_stake}, Maximum stake: £{max_stake}, integer stakes only.\n"
                          f"You have £{self.player_funds} left to play with.\n--->")
            try:
                stake = int(stake.replace("£", ""))  # get rid of the £ sign if the user types one
                if stake > self.player_funds:
                    print(f"A £{stake} stake exceeds your current funds ({self.player_funds}).")
                    continue
                elif min_stake <= stake <= max_stake:
                    confirmation = input(f"Confirm your stake of £{stake}?\n"
                                         "[Y]es, [N]o \n--->").upper()
                    if confirmation != 'Y':
                        print(f"£{stake} stake placed, time to choose your bet!")
                    return stake, all_in_status
                else:
                    print('Invalid stake - please try again and refer to bet criteria.')
            except ValueError:
                print('Invalid stake - please try again and refer to bet criteria.')

    def all_in(self):
        all_in = input(f"The minimum bet exceeds your pot of £{self.player_funds}.\n"
                       f"Would you like to go all in, [Y]es or [N]o?\n--->").upper()
        while True:
            if all_in == 'Y':
                all_in_status = True
                return self.player_funds, all_in_status
            elif all_in == 'N':
                sys.exit(f"Game over, your final pot is {self.player_funds}")
            else:
                print("Invalid options, please try again.")
