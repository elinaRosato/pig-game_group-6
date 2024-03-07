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

    #This method updates the highscores and throws exceptions for errors
    def update_highscores(self, player_name, score):
        if not isinstance(player_name, str):
            raise TypeError("Player name must be a string.")
        if not isinstance(score, int):
            raise TypeError("Score must be an integer.")
        if score < 0:
            raise ValueError("Score must be a non-negative integer.")

        if player_name in self.highscores:
            self.highscores[player_name].append(score)
        else:
            self.highscores[player_name] = [score]
        self.save_highscores()

    #This method updates the player name, or creates one if it doesn´t exist already
    #It also uses error handling
    def update_player_name(self, old_name, new_name):
        if not isinstance(old_name, str) or not isinstance(new_name, str):
            raise TypeError("Player names must be strings.")
        
        if new_name in self.highscores:
            raise KeyError("New player name already used by other player.")
        
        if old_name not in self.highscores:
            raise KeyError("Old player name not found.")
        
        self.highscores[new_name] = self.highscores.pop(old_name)
        self.save_highscores()
