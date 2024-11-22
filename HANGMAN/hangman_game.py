from hangman_game_state import HangmanGameState

class HangmanGame:
    def __init__(self):
        """
        Initializes the Hangman game with a placeholder state and predefined hangman art.
        """
        self.state = None  # Placeholder for the game state
        self.words = [  # List of words for the game
            'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
            'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry',
            'strawberry', 'tangerine', 'watermelon'
        ]
        self.hangman_art = {  # ASCII art for the Hangman
            0: '''
            +---+
            |   |
                |
                |
                |
                |
            =========''',
            1: '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''',
            2: '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''',
            3: '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''',
            4: '''
            +---+
            |   |
            O   |
           /|\\  |
                |
                |
            =========''',
            5: '''
            +---+
            |   |
            O   |
           /|\\  |
           /    |
                |
            =========''',
            6: '''
            +---+
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            ========='''
        }

    def set_state(self, state):
        """
        Sets the current game state.
        :param state: An instance of HangmanGameState.
        """
        self.state = state

    def get_state(self):
        """
        Retrieves the current game state.
        :return: An instance of HangmanGameState.
        """
        return self.state

    def display_hangman(self, tries):
        """
        Displays the Hangman art based on the number of incorrect guesses.
        :param tries: The number of incorrect guesses made.
        """
        print(self.hangman_art.get(tries, "Invalid number of tries"))
