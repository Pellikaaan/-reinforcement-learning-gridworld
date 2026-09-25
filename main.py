from mdp import Action, Cell, COLUMNS, ROWS, GridWorldMDP


def make_move(action: Action, row: int, col: int) -> tuple[int, int]:
    new_row = row
    new_col = col

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


def value_iteration(mdp: GridWorldMDP) -> None:
    actions = (Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT)
    for row in range(mdp.rows):
        for col in range(mdp.columns):
            state = (row, col)
            for action in actions:
                next_states = mdp.transition_probabilities(state, action)
                for next_state, prob in next_states.items():
                    print(f"From {state} taking {action_to_string(action)} -> {next_state} with probability {prob}")




def main() -> None:
     mdp = GridWorldMDP()
     print("States:", sorted(mdp.states()))
     value_iteration(mdp)

if __name__ == "__main__":
     main()

