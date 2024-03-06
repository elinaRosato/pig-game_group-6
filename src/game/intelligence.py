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
    
    def choose_turns(self):
        """
        Choose the number of turns based on the difficulty level.

        Returns:
        - int: The chosen number of turns.
        """
        if self.difficulty == "easy":
            return random.randint(1, 2)  # Choose 1 or 2 turns
        elif self.difficulty == "medium":
            return random.randint(1, 3)  # Choose 1, 2, or 3 turns
        elif self.difficulty == "hard":
            return random.randint(2, 4)  # Choose 2, 3, or 4 turns
    
    def set_difficulty(self, difficulty):
        """
        Set the difficulty level.

        Parameters:
        - difficulty (str): The new difficulty level.

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
    
