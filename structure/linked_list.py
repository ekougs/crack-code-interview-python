from structure.node import Node


class LinkedList:
    def __init__(self, value):
        root = Node(value)
        self.root = root
        self.last = root
        self.__current__ = root

    def push(self, value):
        node = Node(value)
        self.last.next_node = node
        self.last = node
        return self

    def __iter__(self):
        self.__current__ = self.root
        return self

    def next(self):
        if self.__current__ is None:
            raise StopIteration
        else:
            current = self.__current__
            self.__current__ = self.__current__.next_node
            return current

    def __str__(self):
        str_values = []
        for node in self:
            str_values.append(str(node.value))
        return " -> ".join(str_values)
