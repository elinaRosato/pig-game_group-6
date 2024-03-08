import unittest
import os
from highscores import highscore


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
        self.assertTrue(os.path.exists(self.filename))
        self.assertIsInstance(self.highscore.highscores, dict)

    #This tests loading the highscore from a non-existing file
    def test_load_highscores_file_not_found(self):
        os.remove(self.filename)
        self.highscore.load_highscores()
        self.assertEqual(self.highscore.highscores, {})

    #This tests saving the highscore to file
    def test_save_highscores(self):
        self.highscore.highscores = {"Erik": [100, 150]}
        self.highscore.save_highscores()
        self.assertTrue(os.path.exists(self.filename))

    #This tests updating the highscore for an already existing player
    def test_update_highscores_existing_player(self):
        self.highscore.highscores = {"Erik": [100, 150]}
        self.highscore.update_highscores("Erik", 200)
        self.assertEqual(self.highscore.highscores["Erik"], [100, 150, 200])

    #This updates the highscore of a new player
    def test_update_highscores_new_player(self):
        self.highscore.update_highscores("Lena", 300)
        self.assertEqual(self.highscore.highscores["Lena"], [300])

    #This tests updating the name for an existing player
    def test_update_existing_player_name(self):
        self.highscore.highscores = {"Erik": [100, 150]}
        self.highscore.update_player_name("Erik", "Erika")
        self.assertIn("Erika", self.highscore.highscores)
        self.assertNotIn("Erik", self.highscore.highscores)

    #This tests updating a non-existing players name
    def test_update_non_existing_player_name(self):
        with self.assertRaises(KeyError):
            self.highscore.update_player_name("Lena", "Lasse")

    #This tests updating player name to an existing players name
    def test_update_existing_player_new_name(self):
        self.highscore.highscores = {"Erik": [100, 150], "Lena": [200]}
        with self.assertRaises(KeyError):
            self.highscore.update_player_name("Erik", "Lena")

    #This tests updating a player name that is invalid
    def test_invalid_player_name(self):
        with self.assertRaises(KeyError):
            self.highscore.update_player_name("Olof", "Olle")

    #This tests updating the highscore with an invalid input
    def test_update_highscores_invalid_score(self):
        with self.assertRaises(TypeError):
            self.highscore.update_highscores("Erik", "invalid_score")

    #This method tests to input a negative number to the highscore
    def test_update_highscores_negative_score(self):
        with self.assertRaises(ValueError):
            self.highscore.update_highscores("Erik", -50)

    #This method tests updating the highscore with an invalid player name
    def test_update_highscores_invalid_player_name(self):
        with self.assertRaises(TypeError):
            self.highscore.update_highscores(123, 100)

    #This method tests updating the player name with an invalid name
    def test_update_player_name_invalid_names(self):
        with self.assertRaises(TypeError):
            self.highscore.update_player_name(123, "Erika")
        with self.assertRaises(TypeError):
            self.highscore.update_player_name("Erik", 123)