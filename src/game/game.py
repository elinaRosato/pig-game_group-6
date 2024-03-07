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


if __name__ == "__main__":
    game = Game()
    game.play()