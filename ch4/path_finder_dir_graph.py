from collections import deque

"""
Implementation relative to ex 4.2 about path existence in directed graph
"""


def has_path(directed_graph, vrtx1, vrtx2):
    """
    Indicates if path exists in a directed graph between 2 points
    :param directed_graph: a DirectedGraph
    :param vrtx1: an int in graph
    :param vrtx2: another int in graph
    :return: True if path exists, False otherwise
    """
    marked = [vrtx1, vrtx2]
    queue1 = deque(directed_graph.siblings(vrtx1))
    queue2 = deque(directed_graph.siblings(vrtx2))
    while queue1 or queue2:
        sibling1 = -1
        if queue1:
            sibling1 = queue1.pop()
        sibling2 = -1
        if queue2:
            sibling2 = queue2.pop()

        if vrtx2 == sibling1 or vrtx1 == sibling2:
            return True

        if sibling1 not in marked:
            queue1.extend(directed_graph.siblings(sibling1))
            marked.append(sibling1)
        if sibling2 not in marked:
            queue2.extend(directed_graph.siblings(sibling2))
            marked.append(sibling2)

    return False
