class BinaryTreeNode:
    def __init__(self, left=None, right=None, value=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other is not BinaryTreeNode:
            return False
        return other.value == self.value

    def left_empty(self):
        return BinaryTreeNode._empty_node(self.left)

    def right_empty(self):
        return BinaryTreeNode._empty_node(self.right)

    @staticmethod
    def _empty_node(node):
        return node is BinaryTree.EMPTY_NODE


class BinaryTree:
    EMPTY_NODE = BinaryTreeNode()

    def __init__(self, root_key=None):
        if root_key is not None:
            self.root = BinaryTree._leaf(root_key)
        else:
            self.root = BinaryTree.EMPTY_NODE

    @staticmethod
    def _leaf(key):
        return BinaryTreeNode(BinaryTree.EMPTY_NODE, BinaryTree.EMPTY_NODE, key)

    def contains(self, key):
        if self.root is BinaryTree.EMPTY_NODE:
            return False
        return self._contains(self.root, key)

    def _contains(self, node, key):
        if node is BinaryTree.EMPTY_NODE:
            return False
        if node.value == key:
            return True
        elif key > node.value:
            return self._contains(node.right, key)
        return self._contains(node.left, key)

    def insert(self, key):
        if self.contains(key):
            return self.get(key)
        if self.root is BinaryTree.EMPTY_NODE:
            self.root = BinaryTree._leaf(key)
            return self.root
        else:
            return self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value and node.left is self.EMPTY_NODE:
            node.left = BinaryTree._leaf(key)
            return node.left
        elif key > node.value and node.right is self.EMPTY_NODE:
            node.right = BinaryTree._leaf(key)
            return node.right
        elif key < node.value:
            return self._insert(node.left, key)
        elif key > node.value:
            return self._insert(node.right, key)

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node.value == key:
            return node
        elif key > node.value:
            return self._get(node.right, key)
        return self._get(node.left, key)

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is BinaryTree.EMPTY_NODE:
            return 0
        return max(self._size(node.left), self._size(node.right)) + 1
