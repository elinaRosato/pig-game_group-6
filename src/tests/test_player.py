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
