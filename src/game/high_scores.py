import json
import os

#This class manages everything regarding highscores
class HighScore:
    
    #This method loads up the file
    def __init__(self, filename="highscores.json"):
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string.")
        self.filename = filename
        self.create_file_if_not_exists()
        self.highscores = self.load_highscores()

    #This method creates the file if it doesn´t exist already
    def create_file_if_not_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump({}, file)

    #This method opens the file and throws an exception if it´s not found
    def load_highscores(self):
        try:
            with open(self.filename, "r") as file:
                highscores = json.load(file)
        except FileNotFoundError:
            highscores = {}
        return highscores

    #This method saves the highscores
    def save_highscores(self):
        with open(self.filename, "w") as file:
            json.dump(self.highscores, file)