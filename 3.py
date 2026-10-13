import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

def a_star(start, goal):
    q = [(h[start], 0, start, [start])]

    while q:
        f, cost, node, path = heapq.heappop(q)

        if node == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        for next_node, w in graph[node]:
            
            new_cost = cost + w
            heapq.heappush(q, (new_cost + h[next_node],
                               new_cost, next_node, path + [next_node]))

a_star('A', 'D')