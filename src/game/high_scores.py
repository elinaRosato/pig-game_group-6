import json
import os

#This class 
class HighScore:
    #This method
    def __init__(self, filename="highscores.json"):
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string.")
        self.filename = filename
        self.create_file_if_not_exists()
        self.highscores = self.load_highscores()