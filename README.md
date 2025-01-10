# Dijkstra's Shortest Path Algorithm

This Python program implements **Dijkstra's Algorithm** to find the shortest path in a weighted graph. 

## Features
- Supports weighted, undirected graphs.
- Finds the shortest path from a starting node to all other nodes.
- Allows finding the shortest path to a specific target node.
- Handles cases where no path exists between nodes.
- Outputs both the distance and the path.

## How It Works
1. The program uses Dijkstra's algorithm to iteratively calculate the shortest distance to each node.
2. It maintains two main data structures:
   - **Distances**: Tracks the minimum distance from the starting node to each node.
   - **Paths**: Tracks the path taken to reach each node with the shortest distance.

## Input Format
The graph is represented as a dictionary where:
- Keys are node names.
- Values are lists of tuples `(neighbor, weight)` representing edges and their weights.

Example graph:
```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}
