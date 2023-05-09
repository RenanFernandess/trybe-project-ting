class Node:
    def __init__(self, value, next=None, prev=None) -> None:
        self.value = value
        self.next: Node = next
        self.prev: Node = prev
