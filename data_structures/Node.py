class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node
    def __repr__(self) -> str:
        return f"data: {self.data} => next: {self.next_node}"