

class Node(object):
    """
    Each lead in a tree
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    """
    Left child leq father, right child geq father
    """

    def __init__(self):
        self.root = None

    def find_entry(self, entry):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    def find_predecessor(self, entry):
        pass

    def find_successor(self, entry):
        pass

    def insert(self, entry):
        # y = None
        x = self.root
        z = Node(value=entry)
        if self.root is None:
            self.root = z
        elif entry < self.root:
            self.

            # while x is not None:
            #     y = x
            #     if z.value < x.value:
            #         x = x.left
            #     else:
            #         x = x.right
            #     z.p = y
            #     if y is None:
            #         self.root = z
            #     elif z.value < y.value:
            #         y.left = z
            #     else:
            #         y.right = z

    def delete(self, entry):
        pass


if __name__ == "__main__":
    bst = BST()
    bst.insert(entry=1)
    bst.insert(entry=2)
    bst.insert(entry=3)