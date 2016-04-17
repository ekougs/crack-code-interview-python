from structure.node import Node


class LinkedList:
    def __init__(self, value):
        root = Node(value)
        self.root = root
        self.last = root
        self.current = root

    def push(self, value):
        node = Node(value)
        self.last.next_node = node
        self.last = node
        return self

    def __iter__(self):
        self.current = self.root
        return self

    def next(self):
        if self.current is None:
            raise StopIteration
        else:
            current = self.current
            self.current = self.current.next_node
            return current

    def __str__(self):
        str_values = []
        for node in self:
            str_values.append(str(node.value))
        return " -> ".join(str_values)
