import unittest
import os
import highscore


class test_high_score(unittest.TestCase):

    def setUp(self):
        self.filename = "test_highscores.json"
        self.highscore = highscore.HighScore(self.filename)