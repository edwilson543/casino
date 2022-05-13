"""
Base class to define the structure of a simulated game - perhaps not that much of the UI is relevant, as all
confirmation can be got rid of + we can just place and evaluate bets in one go here.

Potential attributes:
    - Number of simulations of a given strategy to complete

Processing/methods:
    - Bet placement (placed on selection which is done by the strategy base class)
    - Bet evaluation, player interaction (adding/taking from pot)
    - Game loop - keep going until we've met criteria

    - Appending the outcome of the simulations to a DataFrame then writing these to a csv. Maybe this should be done
    separately, I think it makes sense here because it's where the data is created - why transport it somewhere else
    before storing.
    I also don't see any point in recording the bet-by-bet progress, as this is
    defined by the bet strategy and the wheel's uniform probability distribution, only the outcome of a strategy and the
    given parameters that led to that outcome.
    - Writing the csv to file at the end of the simulation run (this would likely be a function called from a utils)

The csv fields would be along the lines of:
strategy_name, bet_type_name, bet_type_min_bet, bet_type_max_bet, initial_pot, exit_pot_threshold, win_or_ruin
1 simulation of the strategy would then populate the data in 1 row

These would likely vary by bet strategy, as we might be interested in varying the max_bet for 1-bet strategies, and
recording the bet_type_name, but not for others. What data gets recorded in the output CSV could be an attribute of the
strategy/auto_play base class.

Questions:
1) csv the best option for storing the simulation data?
"""