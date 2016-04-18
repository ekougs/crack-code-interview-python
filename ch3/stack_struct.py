class Stack:
    """
    Stack with O(1) peek, pop, push and min
    """
    def __init__(self, value):
        root = NodeWithMin(value)
        self.root = root
        self.last = root
        self.__current__ = root

    def pop(self):
        element_to_pop = self.last
        self.last = self.last.__next_node__
        return element_to_pop.value

    def peek(self):
        return self.last

    def push(self, value):
        element_to_push = NodeWithMin(value)
        element_to_push.next(self.last)
        self.last = element_to_push
        return self

    def min(self):
        return self.peek().min


class NodeWithMin:
    __next_node__ = None

    def __init__(self, value):
        self.min = value
        self.value = value

    def next(self, node):
        self.__next_node__ = node
        self.min = min(self.min, node.min)
