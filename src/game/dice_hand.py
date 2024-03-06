from dice import Dice

class DiceHand:

    def __init__(self):
        self.dice = Dice()

    def roll_dice(self, num_rolls):
       
        """
        Throw the dice a number of times. 
        
        Parameters:
        num_rolls(int): An integer representing the number of rolls for a round.
        
        Returns:
        A list of integers representing the values from rolling the dice a number of times.
        
        Raises:
        ValueError: If the input number is negative.
        TypeError: If the input is not a number. 
        
        Notes:
        This function uses the PEP 257 convetion for docstrings.
        
        Examples:
        roll_dice(5):
        [5,3,3,1,4]
        """
            
        if num_rolls is not True and num_rolls is not False and isinstance(num_rolls, int) and num_rolls > 0:
            rolls = []
            for _ in range(num_rolls):
                rolls.append(self.dice.roll())
            return rolls
        elif num_rolls <= 0 and num_rolls is not False:
            raise ValueError("Number of rolls must be a non-negative integer.")
        else:
            raise TypeError("Number of rolls must be a positive integer.")
