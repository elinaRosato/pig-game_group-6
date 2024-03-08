from dicehand import DiceHand
from highscores import HighScore
from player import Player
from intelligence import Intelligence
from histogram import Histogram

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
        self.dice_hand = DiceHand()
        self.high_score = HighScore()
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.intelligence = Intelligence()
        self.histogram = Histogram()
    
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
                    oldName = self.player1.name
                    self.player1.change_name(new_name)
                    self.high_score.update_player_name(oldName, new_name)
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

    def set_computer_opponent(self):
        """
        Set up the computer opponent.

        This method prompts the user to choose the difficulty level (easy/medium/hard) for the computer opponent.
        It sets the player2's name to "Computer," marks player2 as a computer, and sets the difficulty level for the intelligence.
        """
        while True:
            difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
            if difficulty in ["easy", "medium", "hard"]:
                self.player2.name = "Computer"
                self.player2.is_computer = True
                self.intelligence.set_difficulty(difficulty)
                break
            else:
                print("Please choose a valid difficulty level (easy/medium/hard).")
    
    def set_human_opponent(self):
        """
        Set up a human opponent.

        This method prompts the user to enter the name of the human opponent and sets it as player2's name.
        """
        opponent_name = input("Enter your opponent's name: ")
        if len(opponent_name.strip()) > 0:
            self.player2.change_name(opponent_name)
    
    def play_round(self, player1, player2):
        """
        Play a round of the game between two players.

        Parameters:
        - player1 (Player): The first player participating in the round.
        - player2 (Player): The second player participating in the round.

        This method takes the current players (player1 and player2) and conducts their turns until one of them
        reaches a score of 100 or more. It then displays the winner and updates the high scores.
        """
        print(f"\nHello, {player1.name}!")
        print(f"You are playing against {player2.name}.")

        player1_score = 0
        player2_score = 0

        while player1_score < 100 and player2_score < 100:
            print(f"{player1.name}'s turn:")
            player1_score += self.take_turn(player1)
            print(f"{player1.name}'s score: {player1_score}")
            if player1_score >= 100:
                print(f"Congratulations, {player1.name}! You win!")
                self.high_score.update_highscores(player1.name, player1_score)
                break;
            else:
                print(f"\n{player2.name}'s turn:")
                if player2.is_computer:
                    turns = self.intelligence.choose_turns()
                    for _ in range(turns):
                        player2_score += self.take_turn(player2)
                        print(f"{player2.name}'s score: {player2_score}")
                        if player2_score >= 100:
                            print(f"Congratulations, {player2.name}! You win!")
                            self.high_score.update_highscores(player2.name, player2_score)
                            break;
                else:
                    player2_score += self.take_turn(player2)
                    print(f"{player2.name}'s score: {player2_score}")
                    if player2_score >= 100:
                        print(f"Congratulations, {player2.name}! You win!")
                        self.high_score.update_highscores(player2.name, player2_score)
                        break;

    def take_turn(self, player):
        """
        Process a player's turn.

        Parameters:
        - player (Player): The current player taking the turn.

        Returns:
        int: The score earned during the turn.

        If the player is a computer, the method determines the number of turns based on the intelligence level.
        If the player is a human, it prompts the player for their decision, including rolling the dice, holding,
        cheating, displaying the histogram, quitting the game, or restarting.

        For human players:
        - 'roll': The player rolls a specified number of dice, and the scores are calculated.
        - 'hold': The player decides to hold their current score.
        - 'cheat': The player activates cheat mode, setting their score to 100.
        - 'histogram': The player displays the current histogram of dice rolls.
        - 'quit': The player quits the game.
        - 'restart': The player restarts the game.

        If a 1 is rolled during the turn, the turn ends, and the score for that turn is 0.
        """
        current_score = 0
        while True:
            if player.is_computer:
                turns = min(self.intelligence.choose_turns(), 5)  # Computer takes up to 5 dice
                rolls = self.dice_hand.roll_dice(turns)
                for roll in rolls:
                    self.histogram.add_roll(roll)
                    print(f"{player.name} rolled: {roll}")
                    if roll == 1:
                        print(f"{player.name} rolled a 1! Turn over.")
                        return 0
                    current_score += roll
                return current_score
            else:
                decision = input("Roll, hold, cheat, histogram, quit or restart? (roll/hold/cheat/histogram/quit/restart): ")
                if decision.lower() == "roll":
                    while True:
                        num_dice_input = input("Enter the number of dice to roll: ")
                        if num_dice_input.isdigit():
                            num_dice = int(num_dice_input)
                            rolls = self.dice_hand.roll_dice(num_dice)
                            for roll in rolls:
                                self.histogram.add_roll(roll)
                                print(f"{player.name} rolled: {roll}")
                                if roll == 1:
                                    print(f"{player.name} rolled a 1! Turn over.")
                                    return 0
                                current_score += roll
                            break
                        else:
                            print("Invalid input. Please enter a valid number.")
                elif decision.lower() == "hold":
                    return current_score
                elif decision.lower() == "cheat":
                    print("Cheat activated! Setting your score to 100.")
                    return 100
                elif decision.lower() == "histogram":
                    self.histogram.display()
                elif decision.lower() == "quit":
                    print("Quitting the game.")
                    exit()
                elif decision.lower() == "restart":
                    print("Restarting the game.")
                    self.play()
                else:
                    print("Invalid input. Please enter 'roll' to roll, 'hold' to hold, 'cheat' to activate cheat mode, 'histogram' to display the histogram, 'quit' to quit, or 'restart' to restart the game.")

    def play_again(self):
        """
        Check if the player wants to play again.

        This method prompts the player to decide whether they want to play another round.
        It returns True if the player chooses 'yes' and False otherwise.
        """
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                print("Loading a new round...")
                return True
            elif play_again == "no":
                print("See you soon!")
                return False
            else:
                print("Please enter a valid option (yes/no).")

if __name__ == "__main__":
    game = Game()
    game.play()