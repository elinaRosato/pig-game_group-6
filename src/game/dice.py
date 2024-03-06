import random

class Dice:
    
    def roll(self):
        
        """
        Generate random number between 1 and 6
        
        Parameters:
        None
        
        Returns:
        int: a random number between 1 and 6(included)
        
        Raises:
        No ValueErrors raised
        
        Notes:
        This function uses the PEP 257 convetion for docstrings.
        
        Examples:
        return random.randint(1, 6)
        5
        
        """
        return random.randint(1, 6)
    
    