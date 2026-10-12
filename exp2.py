from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

print("BFS Traversal:")
bfs(graph, 'A')

print("\nDFS Traversal:")
dfs(graph, 'A')