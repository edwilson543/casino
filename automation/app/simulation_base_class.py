"""Initial ideas on how to structure a strategy ###NOT INTENDED AS ACTUAL CODE"""

from games.roulette.app.roulette_wheel_base_class import RouletteWheel
from pathlib import Path
import pandas as pd

class StrategySimulation:
    """
    SKETCH
    Base class to define the structure of a simulated game - perhaps not that much of the UI is relevant, as all
    confirmation can be got rid of + we can just place and evaluate bets in one go here.
    """
    def __init__(self,
                 n_simulations: int,
                 strategy,
                 playing_wheel: RouletteWheel,
                 data_output_path: Path,
                 data_output_filename: str):
        """
        SKETCH
        Parameters:
        -----------
        n_simulations: The number of simulations of a given strategy to complete
        strategy: The strategy that the simulation is testing
        data_output_path: The path to the file where the data should be stored
        data_output_filename: The name of the file the simulation data should be written to
        """
        self.n_simulations = n_simulations
        self.strategy = strategy
        self.playing_wheel = playing_wheel
        self.data_output_path = data_output_path
        self.data_output_filename = data_output_filename

    def place_individual_bet(self):
        """SKETCH. Bet placement (placed on selection which is done by the strategy base class)"""
        pass
    def bet_evaluation(self):
        """SKETCH. Bet evaluation, resulting in some player interactions (adding/taking from pot)"""
        pass

    def win_or_ruin_individual_run(self):
        """SKETCH. Method to test the strategy once, until either win or ruin is reached"""
        # while not strategy.win and not strategy.ruin:
        #   strategy.keep_placing_more_bets()
        #   outcome = xyz
        #   if win or ruin:
        #       return outcome
        pass

    def run_multiple_simulations(self):
        """SKETCH (more ideas below)"""
        simulation_data = pd.DataFrame()
        # simulation_data.columns = self.strategy.output_data_headers
        for simulation in range(0, self.n_simulations):
            individual_run_outcome = self.win_or_ruin_individual_run()
            pd.concat([simulation_data, individual_run_outcome])
        # simulation_data.to_csv(self.data_output_path / self.data_output_path)
        # The writing part of this could be called from the utils


"""

The csv fields would be along the lines of:
strategy_name, bet_type_name, bet_type_min_bet, bet_type_max_bet, initial_pot, exit_pot_threshold, win_or_ruin
1 simulation of the strategy would then populate the data in 1 row

These would likely vary by bet strategy, as we might be interested in varying the max_bet for 1-bet strategies, and
recording the bet_type_name, but not for others. What data gets recorded in the output CSV could be an attribute of the
strategy/auto_play base class.

Questions:
1) csv the best option for storing the simulation data?
"""