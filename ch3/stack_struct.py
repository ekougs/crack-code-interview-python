"""
Implementation relative to ex 3.2 about stack with O(1) peek, pop, push and min
"""


class Stack:
    """
    Stack with O(1) peek, pop, push and min
    """

    def __init__(self, value):
        root = NodeWithMin(value)
        self.root = root
        self.last = root
        self.__current__ = root
        self.__size__ = 1

    def pop(self):
        element_to_pop = self.last
        self.last = self.last.__next_node__
        self.__size__ -= 1
        return element_to_pop.value

    def peek(self):
        return self.last

    def push(self, value):
        element_to_push = NodeWithMin(value)
        element_to_push.next(self.last)
        self.last = element_to_push
        self.__size__ += 1
        return self

    def min(self):
        return self.peek().min

    def is_empty(self):
        return self.__size__ < 1

    def __iter__(self):
        self.__current__ = self.last
        return self

    def next(self):
        if self.__current__ is None:
            raise StopIteration
        else:
            current = self.__current__
            self.__current__ = self.__current__.__next_node__
            return current

    def __str__(self):
        str_values = []
        for node in self:
            str_values.append(str(node.value))
        return " -> ".join(str_values)


class NodeWithMin:
    __next_node__ = None

    def __init__(self, value):
        self.min = value
        self.value = value

    def next(self, node):
        self.__next_node__ = node
        if node is not None:
            self.min = min(self.min, node.min)
