# pylint: disable=invalid-name
""" Implementation of graph data structure. """

class DirectedGraph():
    """ Directed graph. """

    def __init__(self):
        self.__adj = {} # adjancency list

    def add_edge(self, u, to, cost=1, capacity=1):
        """ Add an edge to the graph """
        edge = {'to': to, 'capacity': capacity, 'cost': cost}
        if u not in self.__adj:
            self.__adj[u] = []
        self.__adj[u].append(edge)

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
            for edge in self.__adj[node]:
                if edge['to'] not in low:
                    scc_dfs(edge['to'])
                low[node] = min(low[node], low[edge['to']])
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
