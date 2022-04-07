from Games.Roulette.app.roulette_wheel_base_class import RouletteWheel
from Games.Roulette.app.roulette_mechanics_action_classes.bet_placement import BetPlacement
from user_interface.command_line.Roulette.definitions.bet_type_defns_user import bet_type_options_user

from typing import Union


class BetPlacementUser(BetPlacement):
    """Purpose of this subclass is to inherit the get_winning_slots and get_potential_winnings
    methods from the BetPlacement class, and
    to add the get_user_bet_choice method which is shown below"""

    def __init__(self,
                 bet_type_id: str,
                 stake: int,
                 playing_wheel: RouletteWheel):
        super().__init__(bet_type_id, stake, playing_wheel)
        self.bet_type = bet_type_options_user[self.bet_type_id]

    def get_user_bet_choice(self) -> Union[int, str, list]:
        """gets user to specify their bet (navigation unique to the bet type)
        then uses generic confirmation by displaying potential payout.
        If confirmation is no, they can place a new bet choice."""
        while True:
            bet_choice = self.bet_type.get_user_bet_choice(playing_wheel=self.playing_wheel)
            confirmation = input(f"Confirm £{self.stake} stake on {bet_choice}?\n"
                                 f"Winning this bet would return: £"
                                 f"{self.get_potential_winnings(self.get_winning_slots(bet_choice))}\n"
                                 f"[Y]es or [N]o\n--->").upper()
            if confirmation != 'Y':
                continue
            else:
                print(f"£{self.stake} placed on {bet_choice}!")
                return bet_choice

from Games.Roulette.definitions.wheel_defns import EuroWheel

bet_placer = BetPlacementUser(bet_type_id='C', stake=10, playing_wheel=EuroWheel())
bet_placer.get_user_bet_choice()
