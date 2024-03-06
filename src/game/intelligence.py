import random

class Intelligence:
    levels = {"easy", "medium", "hard"}

    def __init__(self, difficulty="medium"):
        if not isinstance(difficulty, str):
            raise TypeError("Difficulty level must be a string.")
        if difficulty not in self.levels:
            raise ValueError("Invalid difficulty level. Valid difficulty levels are 'easy', 'medium', or 'hard'.")
        else:
            self.difficulty = difficulty