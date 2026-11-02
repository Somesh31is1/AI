
# Tower of Hanoi using State Space Search

from collections import deque


def tower_of_hanoi(n):
    # Each tuple represents the peg of disks 1, 2, ..., n.
    # Pegs: 0 = A, 1 = B, 2 = C

    start = tuple([0] * n)
    goal = tuple([2] * n)

    queue = deque([start])
    parent = {start: None}
    move_info = {}

    while queue:
        state = queue.popleft()

        if state == goal:
            break

        # Find the top disk on each peg
        top = {}

        for disk, peg in enumerate(state):
            if peg not in top:
                top[peg] = disk

        # Move the top disk to another peg
        for source in range(3):
            if source not in top:
                continue

            disk = top[source]

            for destination in range(3):
                if source == destination:
                    continue

                # Destination must be empty or have
                # a larger disk on top
                if (destination in top and
                        top[destination] < disk):
                    continue

                new_state = list(state)
                new_state[disk] = destination
                new_state = tuple(new_state)

                if new_state not in parent:
                    parent[new_state] = state
                    move_info[new_state] = (
                        disk + 1, source, destination
                    )
                    queue.append(new_state)

    # Reconstruct the solution
    path = []
    current = goal

    while current != start:
        path.append(move_info[current])
        current = parent[current]

    path.reverse()

    names = ["A", "B", "C"]

    for i, (disk, source, destination) in enumerate(path, 1):
        print(
            f"Move {i}: Disk {disk} "
            f"from {names[source]} to {names[destination]}"
        )

    print("Total moves:", len(path))


n = 3
tower_of_hanoi(n)
