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