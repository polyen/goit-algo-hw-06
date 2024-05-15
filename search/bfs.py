from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(graph.nodes[vertex]['ip'], end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited
