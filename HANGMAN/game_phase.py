# Enum to represent the phases of the game
from enum import Enum

class GamePhase(Enum):
    RUNNING = 1  # The game is still ongoing
    FINISHED = 2  # The game has ended
