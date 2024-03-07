class Histogram:
    """
    A class representing a histogram for dice rolls.

    Attributes:
    - counts (dict): A dictionary to store the count of each dice roll.
    """

    def __init__(self):
        """
        Initializes a new instance of the Histogram class.

        The counts dictionary is initialized with counts set to zero for each possible dice roll (1 to 6).
        """
        self.counts = {}
        for i in range(1, 7):
            self.counts[i] = 0