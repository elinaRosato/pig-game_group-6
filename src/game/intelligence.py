import random

class Intelligence:
    """
    Represents the intelligence level of the computer player in a game.
    """

    levels = {"easy", "medium", "hard"}

    def __init__(self, difficulty="medium"):
        """
        Initialize the Intelligence object with a specified difficulty level.

        Parameters:
        - difficulty (str): The difficulty level. Default value is "medium".

        Raises:
        - TypeError: If difficulty is not a string.
        - ValueError: If difficulty is not one of the valid levels ("easy", "medium", "hard").
        """
        if not isinstance(difficulty, str):
            raise TypeError("Difficulty level must be a string.")
        if difficulty not in self.levels:
            raise ValueError("Invalid difficulty level. Valid difficulty levels are 'easy', 'medium', or 'hard'.")
        else:
            self.difficulty = difficulty
    
    
