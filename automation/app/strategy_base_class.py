class StrategicPlayer:
    """
    Base class for defining automated betting strategies - this would be the automation's equivalent of defining
    a player.

    Attributes:
        - Initial player pot
        - Player pot exit threshold
        - Active bet sequence - tracks the last x bets (until the strategy resets), to inform the strategy (as below).
        - Output data fields (i.e. the parameters of interest to record for that simulation - e.g. for the doubling strategy
        we may be interested in the factor that we increase the bet by each time on a losing streak, but this is clearly not
        going to be relevant for a different strategy, so a generic output structure won't do.

    Methods:
        - bet type selection - this represents the strategic bet choice.
        This could range from something as simple as "always bet on red", to any randomly distributed sequence of bets. In
        - stake selection - similar to bet type selection
        - joining this together method - takes the bet/stake selection strategy and returns a given bet.

    Note that both the bet and stake selection must be able to track the player's progress in real-time. For example the
    martingale/doubling strategy needs to know where we are in a losing streak, in order to quantify the bet.

    Subclasses of this strategy will get new attributes/methods as needed - e.g. martingale will have an 'initial bet'
    method, which determines the least bet that can be place and places it, and also a re-set active bet sequence.
    And the additional attribute of the stake multiplication factor.
    """
    pass
