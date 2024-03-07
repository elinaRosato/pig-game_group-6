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
    
    def add_roll(self, roll):
        """
        Adds a dice roll to the histogram.

        Args:
        - roll (int): The value of the dice roll.

        Raises:
        - TypeError: If the roll is not an integer.
        - ValueError: If the roll is not within the range [1, 6].
        """
        if not isinstance(roll, int) or roll is True or roll is False:
            raise TypeError("Roll must be an integer.")
        if roll < 1 or roll > 6:
            raise ValueError("Roll must be an integer within the range [1, 6].")
        self.counts[roll] += 1