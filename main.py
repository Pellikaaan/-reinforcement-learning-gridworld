from enum import IntEnum


ROWS = 4
COLUMNS = 4  # 4x4 grid


class Cell(IntEnum):
    EMPTY = 0
    START = 1
    GOAL = 2
    BLOCKADE = 3


class Action(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def make_move(action: Action, row: int, col: int) -> tuple[int, int]:
    new_row = row
    new_col = col

    # Preserve the fall-through behavior of the original C++ switch.
    if action == Action.UP:
        new_row -= 1

    if action in (Action.UP, Action.DOWN):
        new_row += 1

    if action in (Action.UP, Action.DOWN, Action.LEFT):
        new_col -= 1

    if action in (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT):
        new_col += 1

    return new_row, new_col


def action_to_string(action: Action) -> str:
    if action == Action.UP:
        return "UP"
    if action == Action.DOWN:
        return "DOWN"
    if action == Action.RIGHT:
        return "RIGHT"
    if action == Action.LEFT:
        return "LEFT"

    raise ValueError(f"Unknown action: {action}")


def value_iteration() -> None:
    actions = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)

    for row in range(ROWS):
        for col in range(COLUMNS):
            # TEST
            for action in actions:
                next_row, next_col = make_move(action, row, col)
                print(f"{next_row},{action_to_string(action)},{next_col}")


if __name__ == "__main__":
    value_iteration()
