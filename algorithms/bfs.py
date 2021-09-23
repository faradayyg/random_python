import sys

sys.path.insert(0, "/Users/fridaygodswill/projects/learning/pygame")

from data_structures.graphs import Graph


def bft():
    """Breadth first traversal"""
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(2,3)
    g.insert_edge(2,4)
    g.print_graph()
    queue = []
    visited = [False for i in range(g.vertexes)]
    start = 0
    queue.append(start)
    for i in range(g.vertexes):
        node = g.vertex_array[i].get_head()
        while node is not None:
            if node.data not in visited:
                visited.append(node.data)
                node = node.next_node
            else:
                break

    print(visited, queue)

bft()
