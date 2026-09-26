from typing import TypeAlias
from enum import IntEnum

State: TypeAlias = tuple[int, int]
TransitionProbabilities: TypeAlias = dict[State, float]

ROWS = 4
COLUMNS = 4  # 4x4 grid

class Action(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Cell(IntEnum):
    EMPTY = 0
    START = 1
    GOAL = 2
    BLOCKADE = 3


class GridWorldMDP:
    """State, transition, and reward definitions for the grid world."""

    ACTIONS = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)

    def __init__(self, rows: int = ROWS, columns: int = COLUMNS) -> None:
        self.rows = rows
        self.columns = columns

        self.start_state: State = (0, 0)
        self.goal_state: State = (3, 3)
        self.obstacles: set[State] = {(1, 1), (2, 1)}

        self.goal_reward: float = 1.0
        self.obstacle_reward: float = -10.0
        self.step_reward: float = -1.0

    def states(self) -> set[State]:
        return{(row, column) for row in range(self.rows) for column in range(self.columns)}
    
    def is_terminal(self, state: State) -> bool:
        return state == self.goal_state or state in self.obstacles

    def reward(self, state: State) -> float:
        if state == self.goal_state:
            return self.goal_reward
        elif state in self.obstacles:
            return self.obstacle_reward
        else:
            return self.step_reward

    def transition_probabilities(self, state: State, action: Action) -> TransitionProbabilities:
        if self.is_terminal(state):
            return {state: 1.0}
        r, c = state
        if action == Action.UP:
            next_state = (max(r - 1, 0), c)
        elif action == Action.DOWN:
            next_state = (min(r + 1, self.rows - 1), c)
        elif action == Action.LEFT:
            next_state = (r, max(c - 1, 0))
        elif action == Action.RIGHT:
            next_state = (r, min(c + 1, self.columns - 1))
        else:
            next_state = state
        return {next_state: 1.0}
    

    

