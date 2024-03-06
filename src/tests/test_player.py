import unittest

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

    #Invalid Player Initialization
    def test_invalid_player_initialization_with_integer(self):
        """
        Test creating a player with an invalid name, in this case an integer, and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player(123)
    
    def test_invalid_player_initialization_with_empty_string(self):
        """
        Test creating a player with an invalid name, in this case an empty string, and expect a ValueError.
        """
        with self.assertRaises((ValueError)):
            invalid_player = Player("")

    def test_invalid_player_initialization_with_invalid_is_computer(self):
        """
        Test creating a player with an invalid is_computer value instead of a boolean and expect a TypeError.
        """
        with self.assertRaises((TypeError)):
            invalid_player = Player("Alice", 123)
