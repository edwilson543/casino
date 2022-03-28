from Games.Roulette.app.roulette_base_classes import RouletteWheelWagers
from Games.Roulette.definitions.wheel_defns import euro_wheel_defn, euro_wheel_payout_scaler

euro_wheel = RouletteWheelWagers(slots=euro_wheel_defn, payout_scaler= euro_wheel_payout_scaler)

wheel_dict = {'E' : euro_wheel}

