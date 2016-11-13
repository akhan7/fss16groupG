class Decision:
    """
    Class indicating Decision of a problem
    """

    def __init__(self, name, possible_values):
        """
        @param name: Name of the decision
        @:param possible_values: list of values that the decision can take
        """
        self.name = name
        self.possible_values = possible_values
