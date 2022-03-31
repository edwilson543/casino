from Games.Roulette.definitions.wheel_defns import wheel_options
from Games.Roulette.definitions.game_parameters import pause_durations
from time import sleep


class BetEvaluation:
    """Class to spin the wheel and see if the user wins their bet."""
    def __init__(self, potential_winnings: int, winning_slots: list, user_pot: int, wheel_id: str):
        self.potential_winnings = potential_winnings
        self.winning_slots = winning_slots
        self.user_pot = user_pot
        self.wheel_id = wheel_id
        self.wheel = wheel_options[wheel_id]

    def evaluate_bet(self):
        while True:
            user_ready = input("Type 'SPIN' to spin the wheel!\n--->").upper()
            if user_ready != "SPIN":
                print("Please try spinning the wheel again.")
                continue
            else:
                spin_outcome_num, spin_outcome_col = self.wheel.spin()
                print(f"Wheel spinning...")
                sleep(pause_durations['medium'])
                print(f"Ball has landed on {spin_outcome_num}, ({spin_outcome_col.upper()})!")
                sleep(pause_durations['medium'])
                if spin_outcome_num in self.winning_slots:
                    print(f"Congratulations! You have won £{self.potential_winnings}\n"
                          f"Your pot has increased to £{self.user_pot + self.potential_winnings}")
                    sleep(pause_durations['medium'])
                    return self.potential_winnings
                else:
                    print("Better luck next time, your bet did not win.\n"
                          f"Your pot has decreased to £{self.user_pot}")
                    sleep(pause_durations['medium'])
                    return 0
