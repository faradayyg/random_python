"""Simple implementation of Graph using tha adjacency list."""
import sys

sys.path.insert(0, "/Users/fridaygodswill/projects/learning/pygame/data_structures")

from LinkedList import LinkedList


class Graph:
    def __init__(self, vertexes: int) -> None:
        self.vertexes = vertexes
        self.vertex_array = [LinkedList() for i in range(vertexes)]

    def insert_edge(self, start, end):
        if start >= self.vertexes or end >= self.vertexes:
            raise ValueError("Cannot insert edges to incompatible vertexes")
        self.vertex_array[start].insert_end(end)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertexes):
            print("|", i, end=" | => ")
            temp = self.vertex_array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_node
            print("None")

