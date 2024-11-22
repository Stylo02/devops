import random
from game_phase import GamePhase

class HangmanGameState:
    def __init__(self, word_to_guess=None, guesses=None, incorrect_guesses=None, phase=GamePhase.RUNNING):
        """
        Initialize the game state.
        :param word_to_guess: The word to be guessed (default: randomly chosen).
        :param guesses: List of correctly guessed letters.
        :param incorrect_guesses: List of incorrect guesses.
        :param phase: Current phase of the game (default: RUNNING).
        """
        self.word_to_guess = word_to_guess.upper() if word_to_guess else None  # Word converted to uppercase
        self.guesses = guesses if guesses else []  # Player's correct guesses
        self.incorrect_guesses = incorrect_guesses if incorrect_guesses else []  # Player's incorrect guesses
        self.phase = phase  # Phase of the game

    def add_guess(self, letter):
        """
        Adds a player's guess to the appropriate list (correct or incorrect).
        :param letter: The guessed letter.
        """
        letter = letter.upper()  # Ensure the letter is uppercase
        if letter in self.word_to_guess and letter not in self.guesses:
            self.guesses.append(letter)  # Add to correct guesses
        elif letter not in self.incorrect_guesses:
            self.incorrect_guesses.append(letter)  # Add to incorrect guesses

    def is_word_guessed(self):
        """
        Checks if the player has successfully guessed the word.
        :return: True if all letters in the word are guessed; False otherwise.
        """
        return all(letter in self.guesses for letter in self.word_to_guess)

    def is_game_over(self):
        """
        Determines if the game has ended.
        :return: True if the game is finished; False otherwise.
        """
        if self.phase == GamePhase.FINISHED:
            return True  # The game is already marked as finished
        if len(self.incorrect_guesses) >= 8:  # Check if player has exceeded the guess limit
            self.phase = GamePhase.FINISHED
            return True
        if self.is_word_guessed():  # Check if the word is guessed
            self.phase = GamePhase.FINISHED
            return True
        return False

    def get_hint(self):
        """
        Generates the current hint for the player, revealing guessed letters.
        :return: A string with revealed letters and underscores for hidden ones.
        """
        hint = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                hint += letter
            else:
                hint += "_"
        return hint
