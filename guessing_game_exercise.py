# Guessing Game OOP Interview Exercise
#
# Problem Statement:
# You are tasked with designing a simple guessing game. The game generates a random number within a specified range,
# and the player has to guess the number. The game provides feedback on whether the guess is too high, too low, or correct.
#
# The interviewer may ask the following:
# 1. Implement a class to represent the guessing game.
# 2. Add methods to handle the player's guesses and provide feedback.
# 3. Include a method to check if the game is over.
# 4. Allow the game to be reset with a new random number.
# 5. Extend the functionality to track the number of attempts made by the player.

# Your task is to implement the class and its methods based on the problem statement above.
import random

class GuessingGame:

    def __init__(self, min_value=1, max_value=100, max_attempts=10):
        self.min_value = min_value
        self.max_value = max_value
        self.attempts = 0
        self.number_to_guess = random.randint(self.min_value, self.max_value)
        self.max_attempts = max_attempts
        self.game_over = False        
        
    def make_guess(self, guess: int) -> str:
        if not (self.min_value <= guess <= self.max_value):
            return f"Invalid guess! Please enter a number between {self.min_value} and {self.max_value}."

        if self.game_over:
            return "Game is over. Please reset to play again."
        self.attempts += 1
        if guess < self.number_to_guess:
            feedback = "Too low!"
        elif guess > self.number_to_guess:
            feedback = "Too high!"
        else:
            self.game_over = True
            return f"Correct! You've guessed the number in {self.attempts} attempts."

        if self.attempts >= self.max_attempts:
            self.game_over = True
            return f"Game over! The correct number was {self.number_to_guess}."
        
        return feedback
    
    def get_game_state(self) -> str:
        return f"Attempts: {self.attempts}/{self.max_attempts}, Game Over: {self.game_over}"
        
    def is_game_over(self) -> bool:
        return self.game_over
    
    def reset_game(self):
        self.attempts = 0
        self.number_to_guess = random.randint(1, 100)
        self.game_over = False
        print(f"Game reset. You have {self.max_attempts} attempts to guess the new number.")

if __name__ == "__main__":
    game = GuessingGame()
    print("Welcome to the Guessing Game!")
    print(f"Guess a number between {game.min_value} and {game.max_value}. You have {game.max_attempts} attempts.")

    while not game.is_game_over():
        try:
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            feedback = game.make_guess(guess)
            print(feedback)
            print(game.get_game_state())
        except ValueError:
            print("Please enter a valid integer.")

    print("Thank you for playing!")