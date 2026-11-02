
# A* Search for 8 Puzzle

import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = goal.index(tile)

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row, col = divmod(zero, 3)

    moves = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc

            temp = list(state)
            temp[zero], temp[new_pos] = (
                temp[new_pos], temp[zero]
            )

            neighbors.append(tuple(temp))

    return neighbors


# A* Algorithm
def astar(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path)
                )

    return None


# Display Solution
solution = astar(start)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found.")
