import heapq

def h(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = zero + move

        if 0 <= new_pos < 9:

            if move == -1 and zero % 3 == 0:
                continue

            if move == 1 and zero % 3 == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (h(start, goal), 0, start, [start]))

    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for child in get_neighbors(state):

            if child not in visited:
                new_g = g + 1
                new_f = new_g + h(child, goal)

                heapq.heappush(
                    open_list,
                    (new_f, new_g, child, path + [child])
                )

    return None


print("Enter the start state (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter the goal state:")
goal = tuple(map(int, input().split()))

path = astar(start, goal)

if path:
    print("\nSolution found!")
    print("Number of moves:", len(path) - 1)

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("Failure") 