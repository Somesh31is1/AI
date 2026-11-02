
# Local Beam Search for Travelling Salesman Problem

from itertools import permutations

cities = ["A", "B", "C", "D"]

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


# Calculate total route distance
def route_cost(route):
    total = 0

    for i in range(len(route) - 1):
        total += distance[route[i]][route[i + 1]]

    total += distance[route[-1]][route[0]]

    return total


# Generate neighboring routes
def get_neighbors(route):
    neighbors = []

    for i in range(1, len(route)):
        for j in range(i + 1, len(route)):
            new_route = list(route)

            new_route[i], new_route[j] = (
                new_route[j], new_route[i]
            )

            neighbors.append(tuple(new_route))

    return neighbors


# Local Beam Search
def beam_search(k=3):
    all_routes = [
        (0,) + p for p in permutations(range(1, len(cities)))
    ]

    beam = sorted(all_routes, key=route_cost)[:k]

    while True:
        candidates = set(beam)

        for route in beam:
            candidates.update(get_neighbors(route))

        new_beam = sorted(
            candidates, key=route_cost
        )[:k]

        if new_beam == beam:
            break

        beam = new_beam

    best_route = min(beam, key=route_cost)

    return best_route, route_cost(best_route)


route, cost = beam_search()

print("Best Route:")

for city in route:
    print(cities[city], end=" -> ")

print(cities[route[0]])
print("Total Distance:", cost)
