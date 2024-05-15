import networkx as nx


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(graph.nodes[vertex]['ip'], end=' ')
            visited.add(vertex)
            children = dict(graph[vertex])
            stack.extend(reversed(children))

    return visited
