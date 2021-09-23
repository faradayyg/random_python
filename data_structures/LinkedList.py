from typing import Any, Optional
from Node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def get_head(self):
        return self.head

    def insert_end(self, data: Any):
        data = Node(data)
        if not self.head:
            self.head = data
            return

        node = self.head

        while node.next_node:
            node = node.next_node
        node.next_node = data

    def insert_start(self, data: Any):
        data = Node(data)
        former_head = self.head
        data.next_node = former_head
        self.head = data

    def print_all(self):
        node = self.head
        print(node)
