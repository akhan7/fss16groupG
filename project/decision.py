class Decision:
    """
    Class indicating Decision of a problem
    """

    def __init__(self, name, low, high):
        """
        @param name: Name of the decision
        @param low: minimum value
        @param high: maximum value
        """
        self.name = name
        self.low = low
        self.high = high
