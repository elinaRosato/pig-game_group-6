import unittest
import os
import highscore


class test_high_score(unittest.TestCase):
    #This method sets up the filename and highscore as parameters
    # to be used by the other methods
    def setUp(self):
        self.filename = "test_highscores.json"
        self.highscore = highscore.HighScore(self.filename)

    #This method cleans up the temporary file resources after
    #launching the meethods so they don´t interfere with eachother
    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    #This method tests the initialization of the high score object
    def test_initialization(self):
        """Test initialization of HighScore."""
        self.assertTrue(os.path.exists(self.filename))
        self.assertIsInstance(self.highscore.highscores, dict)

    #This tests if the highscore wasn´t found
    def test_load_highscores_file_not_found(self):
        """Test loading highscores from a non-existent file."""
        os.remove(self.filename)
        self.highscore.load_highscores()
        self.assertEqual(self.highscore.highscores, {})

    #This tests saving the highscore
    def test_save_highscores(self):
        """Test saving highscores to file."""
        self.highscore.highscores = {"Erik": [100, 150]}
        self.highscore.save_highscores()
        self.assertTrue(os.path.exists(self.filename))

    #This tests savnig a highscore for an already existing player
    def test_update_highscores_existing_player(self):
        """Test updating highscores for an existing player."""
        self.highscore.highscores = {"Erik": [100, 150]}
        self.highscore.update_highscores("Erik", 200)
        self.assertEqual(self.highscore.highscores["Erik"], [100, 150, 200])

    #This updates the highscore of a new player
    def test_update_highscores_new_player(self):
        """Test updating highscores for a new player."""
        self.highscore.update_highscores("Lena", 300)
        self.assertEqual(self.highscore.highscores["Lena"], [300])

    #This tests updating the player name
    def test_update_existing_player_name(self):
        """Test updating player name for an existing player."""
        self.highscore.highscores = {"Erik": [100, 150]}
        self.highscore.update_player_name("Erik", "Erika")
        self.assertIn("Erika", self.highscore.highscores)
        self.assertNotIn("Erik", self.highscore.highscores)

    #This tests updating a non-existing player name
    def test_update_non_existing_player_name(self):
        """Test updating player name for a non-existing player."""
        with self.assertRaises(KeyError):
            self.highscore.update_player_name("Lena", "Lasse")

    #This tests updating an existing players name
    def test_update_existing_player_new_name(self):
        """Test updating player name to an existing name."""
        self.highscore.highscores = {"Erik": [100, 150], "Lena": [200]}
        with self.assertRaises(KeyError):
            self.highscore.update_player_name("Erik", "Lena")

    #This tests updating a player name that is invalid
    def test_invalid_player_name(self):
        """Test updating player name with an invalid old name."""
        with self.assertRaises(KeyError):
            self.highscore.update_player_name("Olof", "Olle")
