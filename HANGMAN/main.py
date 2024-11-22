import random
from hangman_game import HangmanGame
from hangman_game_state import HangmanGameState
from game_phase import GamePhase

def main():
    # Initialize the game
    game = HangmanGame()
    state = HangmanGameState(word_to_guess=random.choice(game.words))  # Select a random word from the game
    game.set_state(state)

    print("Welcome to Hangman!")  # Introduction message

    while not game.get_state().is_game_over():  # Continue until the game ends
        current_state = game.get_state()

        # Display the hangman art and hint
        game.display_hangman(len(current_state.incorrect_guesses))
        print("Word: ", " ".join(current_state.get_hint()))  # Display the hint

        # Prompt the player for input
        guess = input("Enter a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in current_state.guesses or guess in current_state.incorrect_guesses:
            print("You already guessed that letter!")
            continue

        # Add the guess to the game state
        current_state.add_guess(guess)

        # Check if the game is over
        if current_state.is_game_over():
            if current_state.is_word_guessed():  # Player wins
                print("Congratulations! You won!")
            else:  # Player loses
                print(f"You lost! The word was '{current_state.word_to_guess}'.")
            break

        # Update the game state
        game.set_state(current_state)

if __name__ == "__main__":
    main()
