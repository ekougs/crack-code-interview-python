from unittest import TestCase

from ch4.path_finder_dir_graph import has_path
from structure.directed_graph import DirectedGraph


class PathFinderTest(TestCase):
    graph = DirectedGraph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)

    graph.add_edge(2, 3)

    graph.add_edge(3, 2)
    graph.add_edge(3, 5)

    graph.add_edge(4, 2)
    graph.add_edge(4, 3)

    def test_should_find_path_between_5_and_2(self):
        self.assertTrue(has_path(PathFinderTest.graph, 2, 5))

    def test_should_not_find_path_between_1_and_5(self):
        self.assertFalse(has_path(PathFinderTest.graph, 1, 5))

    def test_should_not_find_path_between_2_and_1(self):
        self.assertFalse(has_path(PathFinderTest.graph, 2, 1))

    def test_should_not_find_path_between_1_and_2(self):
        self.assertFalse(has_path(PathFinderTest.graph, 1, 2))
