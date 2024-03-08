class Player:
    """
    Represents a player in the game.

    Attributes:
    - name (str): The name of the player.
    - is_computer (bool): Indicates whether the player is controlled by the computer.
    """

    def __init__(self, name, is_computer=False):
        """
        Initialize a Player instance with the provided name and computer control status.

        Parameters:
        - name (str): The name of the player.
        - is_computer (bool): Indicates whether the player is controlled by the computer.
          Default value is False.

        Raises:
        - TypeError: If name is not a string or is_computer is not a boolean.
        - ValueError: If name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        else:
            self.name = name
             
        if not isinstance(is_computer, bool):
            raise TypeError("Is computer must be a boolean.")
        else:
            self.is_computer = is_computer

    def change_name(self, new_name):
        """
        Change the name of the player.

        Parameters:
        - new_name (str): The new name for the player.

        Raises:
        - TypeError: If new_name is not a string.
        - ValueError: If new_name is an empty string.
        """
        if not isinstance(new_name, str):
            raise TypeError("New name must be a string.")
        elif len(new_name) == 0:
            raise ValueError("New name must be a non-empty string.")
        else:
            self.name = new_name