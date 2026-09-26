from mdp import Action, Cell, COLUMNS, ROWS, GridWorldMDP, TransitionProbabilities


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


def value_iteration(mdp: GridWorldMDP) -> TransitionProbabilities:
    gamma = 0.9
    theta = 0.0001

    values: TransitionProbabilities = {
        state: 0.0 for state in mdp.states()
    }

    iteration = 0

    while True:
        new_values = values.copy()
        delta = 0.0

        for state in mdp.states():

            if mdp.is_terminal(state):
                continue

            action_values = []

            for action in mdp.ACTIONS:
                action_value = 0.0

                next_states = mdp.transition_probabilities(state, action)

                for next_state, probability in next_states.items():
                    reward = mdp.reward(next_state)

                    action_value += probability * (
                        reward + gamma * values[next_state]
                    )

                action_values.append(action_value)

            new_values[state] = max(action_values)

            delta = max(
                delta,
                abs(new_values[state] - values[state])
            )

        values = new_values
        iteration += 1

        print(f"Iteration {iteration}, delta = {delta}")

        if delta < theta:
            break

    return values

def extract_policy(
    mdp: GridWorldMDP,
    values: dict[State, float],
    gamma: float = 0.9
) -> TransitionProbabilities:

    policy: TransitionProbabilities = {}

    for state in mdp.states():

        if mdp.is_terminal(state):
            continue

        best_action = None
        best_value = float("-inf")

        for action in mdp.ACTIONS:
            action_value = 0.0

            next_states = mdp.transition_probabilities(state, action)

            for next_state, probability in next_states.items():
                reward = mdp.reward(next_state)

                action_value += probability * (
                    reward + gamma * values[next_state]
                )

            if action_value > best_value:
                best_value = action_value
                best_action = action

        policy[state] = best_action

    return policy

def main() -> None:
    mdp = GridWorldMDP()
    values = value_iteration(mdp)
    policy = extract_policy(mdp, values)

    print("\nOptimal policy:")

    for state in sorted(policy):
        print(
            state,
            "->",
            action_to_string(policy[state])
        )
    print("\nConverged values:")
    for state in sorted(values):
        print(state, round(values[state], 3))


if __name__ == "__main__":
    main()

