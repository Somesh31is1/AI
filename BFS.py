
# BFS for Path Finding

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


start = "A"
goal = "F"

path = bfs(start, goal)

if path:
    print("Path Found:", " -> ".join(path))
    print("Number of edges:", len(path) - 1)
else:
    print("No path found.")
