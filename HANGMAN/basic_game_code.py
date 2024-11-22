import random  # Importing random for choosing a word randomly from the list

# List of words the game will randomly choose from
words = [
    'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew',
    'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry',
    'strawberry', 'tangerine', 'watermelon'
]

# Dictionary storing hangman drawings for each stage of the game
hangman_art = {
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

# Function to display the hangman drawing based on the number of incorrect guesses
def display_hangman(tries):
    """
    Prints the hangman ASCII art based on the number of tries.
    """
    print(hangman_art[tries])

# Function to generate the current hint for the player
def display_hint(word, guessed_letters):
    """
    Generates and returns the current progress of the word being guessed.
    For every letter in the word:
        - If the letter has been guessed, include it in the hint.
        - If not, display "_" (underscore) for that letter.
    """
    hint = ""
    for letter in word:
        if letter in guessed_letters:  # If the letter is already guessed
            hint += letter  # Reveal the letter
        else:
            hint += "_"  # Otherwise, keep it hidden as "_"
    return hint

# Main function that runs the Hangman game
def main():
    """
    Implements the Hangman game logic step by step.
    """
    word = random.choice(words)  # Randomly selects a word from the words list
    guessed_letters = []  # List to store all letters guessed by the player
    tries = 0  # Counter to track the number of incorrect guesses

    print("Welcome to Hangman!")  # Introduction message

    # Gameplay loop - Keeps running until the player wins or loses
    while tries < 6:  # The player has 6 chances
        display_hangman(tries)  # Show the current hangman drawing based on incorrect guesses

        # Generate and display the current state of the word (with guesses revealed)
        hint = display_hint(word, guessed_letters)
        print("Word: ", " ".join(hint))  # Add spaces between the letters for better readability

        # Check if the player has successfully guessed the word
        if hint == word:  # If the current hint matches the word
            print("Congratulations! You won!")  # Player wins
            break

        # Ask the player to guess a letter
        guess = input("Enter a letter: ").lower()  # Convert input to lowercase for consistency

        # Check if the input is valid (must be a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue  # Skip this iteration and ask again

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")  # Inform the player
            continue  # Skip this iteration and ask again

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess not in word:
            print(f"'{guess}' is not in the word!")  # Inform the player about the incorrect guess
            tries += 1  # Increment the incorrect guess counter

    # End of the game - Check if the player lost
    if tries == 6:  # If the player runs out of tries
        display_hangman(tries)  # Display the final hangman drawing
        print(f"You lost! The word was '{word}'.")  # Reveal the word to the player

# Run the game
if __name__ == "__main__":
    main()
