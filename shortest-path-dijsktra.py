def shortest_path(graph, start, target=None):
    """
    Find the shortest paths in a weighted graph using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary where keys are node names and values are lists of tuples 
                      (neighbor, weight) representing edges and their weights.
        start (str): The starting node.
        target (str, optional): The specific target node for which the shortest path is desired. 
                                 If None, the algorithm finds shortest paths to all nodes.

    Returns:
        tuple: A dictionary of distances and a dictionary of paths.
    """
    # Initialize unvisited nodes, distances, and paths
    unvisited = list(graph.keys())
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]

    while unvisited:
        # Select the unvisited node with the smallest distance
        current = min(unvisited, key=lambda node: distances[node])

        # Update distances and paths for neighbors of the current node
        for neighbor, weight in graph[current]:
            if distances[current] + weight < distances[neighbor]:
                distances[neighbor] = distances[current] + weight
                paths[neighbor] = paths[current] + [neighbor]

        unvisited.remove(current)

    # If a specific target is provided, print its distance and path
    if target:
        if distances[target] == float('inf'):
            print(f"No path from {start} to {target}.")
        else:
            print(f"Shortest path from {start} to {target}:")
            print(f"Distance: {distances[target]}")
            print(f"Path: {' -> '.join(paths[target])}")
    else:
        # Print all shortest paths from the start node
        print(f"Shortest paths from {start}:")
        for node, distance in distances.items():
            if node == start:
                continue
            if distance == float('inf'):
                print(f"No path to {node}.")
            else:
                print(f"\n{start} -> {node} distance: {distance}")
                print(f"Path: {' -> '.join(paths[node])}")

    return distances, paths


# Example usage
if __name__ == "__main__":
    my_graph = {
        'A': [('B', 5), ('C', 3), ('E', 11)],
        'B': [('A', 5), ('C', 1), ('F', 2)],
        'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
        'D': [('C', 1), ('E', 9), ('F', 3)],
        'E': [('A', 11), ('C', 5), ('D', 9)],
        'F': [('B', 2), ('D', 3)]
    }

    shortest_path(my_graph, 'A', 'F')
