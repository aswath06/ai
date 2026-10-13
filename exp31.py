
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

def a_star(start, goal):
    # (priority f(n), actual cost g(n), node, path)
    queue = [(heuristic[start], 0, start, [])]
    best_cost = {start: 0}
    while queue:
        priority, cost, node, path = heapq.heappop(queue)
        # Skip outdated queue entries
        if cost != best_cost.get(node):
            continue
        path = path + [node]
        # Check whether the goal is reached
        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return
        # Explore neighboring nodes
        for neighbour, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < best_cost.get(neighbour, float('inf')):
                best_cost[neighbour] = new_cost
                # A* formula: f(n) = g(n) + h(n)
                new_priority = new_cost + heuristic[neighbour]
                heapq.heappush(
                        queue,
                    (new_priority, new_cost, neighbour, path)
                )
    print("No path found")


a_star('A', 'D')
