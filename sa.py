
import random
import math

# Calculate number of attacking queen pairs
def cost(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate all neighboring states
def get_neighbors(board):
    neighbors = []
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            new_board = board.copy()
            new_board[i], new_board[j] = new_board[j], new_board[i]

            neighbors.append((new_board, (i, j), cost(new_board)))

    return neighbors


# Simulated Annealing Algorithm
def simulated_annealing():

    # Initial random state
    current = [3, 1, 2, 0, 5, 7, 4, 6]

    temperature = 100.0
    cooling_rate = 0.95
    min_temperature = 0.01

    step = 1

    print("Initial State:", current)
    print("Initial Cost:", cost(current))

    while temperature > min_temperature:

        current_cost = cost(current)

        # Check goal state
        if current_cost == 0:
            print("\nGoal State Reached!")
            return current

        print("\nSTEP", step)
        print("Temperature:", round(temperature, 3))

        # Generate neighboring states
        neighbors = get_neighbors(current)

        print("\nNeighbor States and Costs:")

        for board, pair, value in neighbors:
            print(
                f"Swap (x{pair[0]}, x{pair[1]}) "
                f"=> {board}, Cost = {value}"
            )

        # Randomly select one neighbor
        new_board, pair, new_cost = random.choice(neighbors)

        print("\nCurrent State:", current)
        print("Current Cost:", current_cost)

        print("Selected Neighbor:", new_board)
        print("Neighbor Cost:", new_cost)

        delta = new_cost - current_cost

        # Accept better solution
        if delta < 0:
            current = new_board
            print("Better solution accepted!")

        # Accept worse solution with probability
        else:
            probability = math.exp(-delta / temperature)
            r = random.random()

            print("Acceptance Probability:", round(probability, 4))
            print("Random Value:", round(r, 4))

            if r < probability:
                current = new_board
                print("Worse solution accepted!")
            else:
                print("Neighbor rejected!")

        # Reduce temperature
        temperature *= cooling_rate

        print("New Current State:", current)
        print("New Cost:", cost(current))

        step += 1

    return current if cost(current) == 0 else None


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


# Main program with random restart
solution = None

for attempt in range(100):

    print("\n========== ATTEMPT", attempt + 1, "==========")

    solution = simulated_annealing()

    if solution is not None:
        break


# Display final result
if solution is not None:

    print("\nSolution Found!")
    print("Final Solution:", solution)
    print("Final Cost:", cost(solution))

    print("\nFinal Chessboard:")
    display_board(solution)

else:
    print("\nSolution not found. Try again.")
