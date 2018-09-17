# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-many-public-methods

import unittest
from structures.Graph import DirectedGraph

class testDirectedGraph(unittest.TestCase):
    def test_strong_components(self):
        g = DirectedGraph()
        edges = [(0, 1), (1, 3), (3, 0), (3, 2), (2, 4), (4, 2), (4, 5), (5, 6), (6, 7)]
        for e in edges:
            g.add_edge(*e)
        components = sorted([sorted(c) for c in g.strong_components()])
        self.assertEqual(components, [[0, 1, 3], [2, 4], [5], [6], [7]])
