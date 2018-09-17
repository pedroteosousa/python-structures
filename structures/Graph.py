# pylint: disable=invalid-name
""" Implementation of graph data structure. """

class DirectedGraph():
    """ Directed graph. """

    def __init__(self):
        self.__adj = {} # adjancency list

    def add_edge(self, u, to, weight=1):
        """ Add an edge to the graph. """
        edge = {'to': to, 'weight': weight}
        if u not in self.__adj:
            self.__adj[u] = {}
        if to not in self.__adj[u]:
            self.__adj[u][to] = []
        self.__adj[u][to].append(edge)

    def strong_components(self):
        """ Get strongly connected components. """
        components = []

        time = 0
        seen, low = {}, {}
        stack = []
        def scc_dfs(node):
            nonlocal time, seen, low, stack
            seen[node] = low[node] = time = time + 1
            stack.append(node)
            if node in self.__adj:
                for to in self.__adj[node]:
                    if to not in low:
                        scc_dfs(to)
                    low[node] = min(low[node], low[to])
            if low[node] == seen[node]:
                new_component = []
                while stack:
                    new_component.append(stack.pop())
                    low[new_component[-1]] = len(self.__adj) + 1
                    if new_component[-1] == node:
                        break
                components.append(new_component)

        for node in self.__adj:
            if node not in seen:
                scc_dfs(node)
        return components
