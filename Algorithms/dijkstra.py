def dijkstra(nodes, distances):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = 'A'
    # store preceeding nodes
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbor, distance in distances[current].items():
            if neighbor not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbor] is None or unvisited[neighbor] > newDistance:
                unvisited[neighbor] = newDistance
        # target distance up to this point found,
        #  set current node as target node
        visited[current] = currentDistance
        del unvisited[current]

        if not unvisited: break

        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited

nodes = ('A', 'B', 'C', 'D', 'E', 'Z')
distances = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'C': 1},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 5},
    'Z': {'D': 6, 'E': 5}}

print(dijkstra(nodes, distances))