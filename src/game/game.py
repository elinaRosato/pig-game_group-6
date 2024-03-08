import dicehand
import highscores
import player
import intelligence
import histogram

class Game:
    """
    Represents the game engine.

    Attributes:
    dice_hand (DiceHand): An instance of the DiceHand class for rolling dice.
    - high_score (HighScore): An instance of the HighScore class for tracking high scores.
    - player1 (Player): An instance of the Player class representing the first player.
    - player2 (Player): An instance of the Player class representing the second player.
    - intelligence (Intelligence): An instance of the Intelligence class for computer opponent decisions.
    - histogram (Histogram): An instance of the Histogram class for tracking dice roll frequencies.
    """

    def __init__(self):
        """
        Initializes a new game with default settings.
        """
        self.dice_hand = dicehand.DiceHand()
        self.high_score = highscores.HighScore()
        self.player1 = player.Player("Player1")
        self.player2 = player.Player("Player2")
        self.intelligence = intelligence.Intelligence()
        self.histogram = histogram.Histogram()
    
    def play(self):
        """
        Plays a round of Pig.

        This method manages the flow of the game, including player setup, rounds, and determining the winner.
        """
        print("Welcome to Pig! The Hog variant")
        while True:
            self.get_player_name()
            self.change_player_name()
            self.set_opponent()
            self.play_round(self.player1, self.player2)
            another_round = self.play_again()
            if not another_round:
                print("Thanks for playing!")
                break
    
    def get_player_name(self):
        """
        Get the player's name.

        Loops until a non-empty name is entered.
        Sets the entered name as the player1's name using change_name method.
        """
        while True:
            player_name = input("Enter your name: ")
            if player_name.strip():
                self.player1.change_name(player_name)
                break
            else:
                print("Please enter a non-empty name.")
    
    def change_player_name(self):
        """
        Change the player's name.

        Asks the player if they want to change their name.
        If 'yes', loops until a non-empty new name is entered.
        Sets the new name as player1's name using change_name method.
        Updates the high score with the player's new name.
        """
        change_name = input("Do you want to change your name? (yes/no): ")
        if change_name.lower() == "yes":
            while True:
                new_name = input("Enter your new name: ")
                if len(new_name.strip()) > 0:
                    self.player1.change_name(new_name)
                    self.high_score.update_player_name(self.player1.name, new_name)
                    break
                else:
                    print("Please enter a non-empty name.")
    
    def set_opponent(self):
        """
        Set the opponent for the game.

        This method prompts the user to choose whether to play against the computer or another human player.
        It then calls the corresponding method to set up the opponent.
        """
        while True:
            opponent_choice = input("Do you want to play against the computer? (yes/no): ").lower()
            if opponent_choice == "yes":
                self.set_computer_opponent()
                break
            elif opponent_choice == "no":
                self.set_human_opponent()
                break
            else:
                print("Please enter a valid option (yes/no).")



if __name__ == "__main__":
    game = Game()
    game.play()