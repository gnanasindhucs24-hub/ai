

from itertools import combinations

# Calculate number of attacking queen pairs
def cost(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate all neighboring states by swapping queens
def get_neighbors(board):
    neighbors = []

    for i, j in combinations(range(len(board)), 2):
        new_board = board.copy()
        new_board[i], new_board[j] = new_board[j], new_board[i]

        neighbors.append((new_board, (i, j), cost(new_board)))

    return neighbors


# Display chessboard
def display_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Hill Climbing Algorithm
def hill_climbing():
    # Given initial state
    current = [3, 1, 2, 0]
    step = 1

    print("Initial State:", current)
    print("Initial Cost:", cost(current))

    while True:
        print("\nSTEP", step)

        neighbors = get_neighbors(current)

        print("Neighbor States and Costs:")

        for board, pair, value in neighbors:
            print(
                f"Swap (x{pair[0]}, x{pair[1]}) "
                f"=> {board}, Cost = {value}"
            )

        # Select minimum cost neighbor.
        # combinations() ensures tie-breaking by smallest pair.
        best_board, best_pair, best_cost = min(
            neighbors, key=lambda x: (x[2], x[1])
        )

        print("\nCurrent Cost:", cost(current))
        print("Best Neighbor:", best_board)
        print("Best Cost:", best_cost)

        # Stop if no improvement
        if best_cost >= cost(current):
            print("\nAlgorithm Terminated!")
            print("No better neighbor found.")
            break

        current = best_board

        print("New Current State:", current)

        if best_cost == 0:
            print("\nGoal State Reached!")
            break

        step += 1

    print("\nFinal Solution:", current)
    print("Final Cost:", cost(current))

    print("\nFinal Chessboard:")
    display_board(current)


# Main program
hill_climbing()
                                   