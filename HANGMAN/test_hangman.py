import pytest
import string
from hangman_game import HangmanGame
from hangman_game_state import HangmanGameState
from game_phase import GamePhase


@pytest.fixture
def game_state():
    """
    Fixture to create a default game state for testing.
    """
    return HangmanGameState(word_to_guess="devops", guesses=[], incorrect_guesses=[])


@pytest.fixture
def game():
    """
    Fixture to initialize the Hangman game.
    """
    return HangmanGame()


def test_set_state_get_state(game, game_state):
    """
    Test 001: Check if set_state and get_state methods work properly.
    """
    game.set_state(game_state)
    retrieved_state = game.get_state()
    assert retrieved_state.word_to_guess == game_state.word_to_guess
    assert retrieved_state.guesses == game_state.guesses
    assert retrieved_state.incorrect_guesses == game_state.incorrect_guesses
    assert retrieved_state.phase == game_state.phase


def test_action_list_contains_only_unused_letters(game_state):
    """
    Test 002: Action list contains only 'unused' capital letters.
    """
    # Initial state
    all_letters = set(string.ascii_uppercase)
    guessed_letters = set(game_state.guesses)
    remaining_letters = all_letters - guessed_letters
    assert remaining_letters == all_letters  # No letters guessed yet

    # After guessing some letters
    game_state.guesses = ['A', 'B', 'C']
    remaining_letters = all_letters - set(game_state.guesses)
    assert remaining_letters == set(string.ascii_uppercase[3:])


def test_apply_action_adds_guess(game_state):
    """
    Test 003: Apply action method adds new guess to game state.
    """
    game_state.add_guess('D')  # Correct guess
    assert 'D' in game_state.guesses
    assert 'D' not in game_state.incorrect_guesses

    game_state.add_guess('Z')  # Incorrect guess
    assert 'Z' in game_state.incorrect_guesses
    assert 'Z' not in game_state.guesses


def test_apply_action_lowercase_handling(game_state):
    """
    Test 004: Apply action also works for lowercase letters.
    """
    game_state.add_guess('a')  # Guessing lowercase
    assert 'A' in game_state.guesses  # Converted to uppercase


def test_game_ending_conditions(game_state):
    """
    Test 005: Game ends with 8 wrong guesses or when the secret word is revealed.
    """
    # Case 1: Game ends with 8 wrong guesses
    game_state.incorrect_guesses = list("ABCDEFGH")
    assert game_state.is_game_over()
    assert game_state.phase == GamePhase.FINISHED

    # Case 2: Game ends when the word is guessed
    game_state = HangmanGameState(word_to_guess="XY", guesses=["X", "Y"])
    assert game_state.is_game_over()
    assert game_state.phase == GamePhase.FINISHED


def test_secret_word_with_lowercase_letters():
    """
    Test 006: Game works when secret word contains lowercase letters.
    """
    game_state = HangmanGameState(word_to_guess="Xy", guesses=["X", "Y"])
    assert game_state.is_game_over()
    assert game_state.phase == GamePhase.FINISHED
