# tested on python3.8 version

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        yield self.value
        if self.left is not None:
            for node in self.left:
                yield node
        if self.right is not None:
            for node in self.right:
                yield node

if __name__ == '__main__':

    # initialize and construct tree
    node_one = Tree(1) # leaf node
    node_two = Tree(2) # leaf node
    node_three = Tree(3) # leaf node
    node_four = Tree(4) # leaf node
    node_five = Tree(5, node_one, node_two)
    node_six = Tree(6, node_three, node_four)
    root = Tree(7, node_five, node_six)

    # iteration will print the tree in Pre-Order Traversal as defined in __iter__ function
    for node in root:
        print(node, end=" ")