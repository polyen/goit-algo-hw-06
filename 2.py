from data import get_graph
from search.bfs import bfs
from search.dfs import dfs

if __name__ == "__main__":
    G = get_graph()

    print('Результати пошуку BFS:')
    bfs(G, 1)
    print('\nРезультати пошуку DFS:')
    dfs(G, 1)
