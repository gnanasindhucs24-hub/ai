
import heapq

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Initial state (0 represents blank)
initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)


# Calculate Manhattan distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):

    neighbors = []
    zero = state.index(0)

    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_pos = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def solve_puzzle(initial):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (heuristic(initial), 0, initial, [initial])
    )

    visited = set()

    while priority_queue:

        f, g, state, path = heapq.heappop(priority_queue)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Display puzzle
def display(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


# Main program
print("Initial State:")
display(initial)

solution = solve_puzzle(initial)

if solution:

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):

        print("Step", step)
        display(state)

else:
    print("No solution exists.")
