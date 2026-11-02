
# DFS for Water Jug Problem

def water_jug_dfs():
    capacity_a = 4
    capacity_b = 3
    goal = 2

    stack = [((0, 0), [])]
    visited = set()

    while stack:
        (a, b), path = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == goal:
            return path

        # 1. Fill Jug A
        # 2. Fill Jug B
        # 3. Empty Jug A
        # 4. Empty Jug B
        # 5. Pour A into B
        # 6. Pour B into A

        pour_a_to_b = min(a, capacity_b - b)
        pour_b_to_a = min(b, capacity_a - a)

        next_states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (a - pour_a_to_b, b + pour_a_to_b),
            (a + pour_b_to_a, b - pour_b_to_a)
        ]

        for state in next_states:
            if state not in visited:
                stack.append((state, path))

    return None


solution = water_jug_dfs()

if solution:
    print("Solution States:")

    for a, b in solution:
        print("Jug A:", a, "litres, Jug B:", b, "litres")
else:
    print("No solution found.")
