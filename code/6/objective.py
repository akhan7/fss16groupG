class Objective:
    """
    Class indicating Objective of a problem
    """

    def __init__(self, name, do_minimize=True, low=0, high=1):
        """
        @param name: Name of the objective
        @param do_minimize: Flag indicating if objective has to be minimized or maximized
        """
        O.__init__(self, name=name, do_minimize=do_minimize, low=low, high=high)

    def normalize(self, val):
        return (val - self.low) / (self.high - self.low)
