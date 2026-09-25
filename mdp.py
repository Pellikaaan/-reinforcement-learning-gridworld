from typing import TypeAlias
from main import Action, COLUMNS, ROWS

State: TypeAlias = tuple[int, int]
TransitionProbabilities: TypeAlias = dict[State, float]


class GridWorldMDP:
    """State, transition, and reward definitions for the grid world."""

    ACTIONS = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)

    def __init__(self, rows: int = ROWS, columns: int = COLUMNS) -> None:
        self.rows = rows
        self.columns = columns