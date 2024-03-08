import unittest
from player import Player 


class TestPlayer(unittest.TestCase):

    # Valid Player Initialization
    def test_valid_player_initialization_default(self):
        """
        Test creating a player with a valid name and default is_computer value.
        """
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")
        self.assertFalse(player.is_computer)

    def test_valid_player_initialization_is_computer(self):
        """
        Test creating a player with a valid name and is_computer=True.
        """
        player = Player("Alice", True)
        self.assertEqual(player.name, "Alice")
        self.assertTrue(player.is_computer)

    def test_valid_player_initialization_is_not_computer(self):
        """
        Test creating a player with a valid name and is_computer=False.
        """
        player = Player("Alice", False)
        self.assertEqual(player.name, "Alice")
        self.assertFalse(player.is_computer)

    #Invalid Player Initialization with an invalid player name
    def test_invalid_player_initialization_with_integer(self):
        """
        Test creating a player with an invalid name, in this case an integer, and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player(123)
    
    def test_invalid_player_initialization_with_float(self):
        """
        Test creating a player with an invalid name, in this case a float, and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player(1.23)
        
    def test_invalid_player_initialization_with_boolean(self):
        """
        Test creating a player with an invalid name, in this case a boolean, and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player(True)
        
    def test_invalid_player_initialization_with_array(self):
        """
        Test creating a player with an invalid name, in this case an array, and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player(["Alice", "Bob"])

    def test_invalid_player_initialization_with_empty_string(self):
        """
        Test creating a player with an invalid name, in this case an empty string, and expect a ValueError.
        """
        with self.assertRaises((ValueError)):
            invalid_player = Player("")

    """
    def test_invalid_player_initialization_with_None(self):
        #Test creating a player with an invalid name, in this case None, and expect a ValueError.
        with self.assertRaises((ValueError)):
            invalid_player = Player(None)
    """

    #Invalid Player Initialization with an invalid is_computer type
    def test_invalid_player_initialization_with_invalid_is_computer_integer(self):
        """
        Test creating a player with an invalid is_computer value instead of a boolean and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player("Alice", 123)

    def test_invalid_player_initialization_with_invalid_is_computer_float(self):
        """
        Test creating a player with an invalid is_computer value instead of a boolean and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player("Alice", 1.23)
    
    def test_invalid_player_initialization_with_invalid_is_computer_string(self):
        """
        Test creating a player with an invalid is_computer value instead of a boolean and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player("Alice", "yes")

    # Change Name
    def test_change_name_valid_new_name(self):
        """
        Test changing the name of a player with a valid new name.
        """
        player = Player("Bob")
        player.change_name("Charlie")
        self.assertEqual(player.name, "Charlie")
    
    def test_change_name_invalid_new_name(self):
        """
        Test changing the name of a player with an invalid new name and expect a TypeError or ValueError.
        """
        player = Player("Bob")

        # Test case 1: Invalid new name (integer)
        with self.assertRaises((TypeError)):
            player.change_name(123)
        
        # Test case 1: Invalid new name (boolean)
        with self.assertRaises((TypeError)):
            player.change_name(True)

        # Test case 2: Invalid new name (empty string)
        with self.assertRaises((ValueError)):
            player.change_name("")

if __name__ == '__main__':
    unittest.main()
