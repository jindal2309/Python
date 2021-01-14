"""
Problem Description: Given two binary tree, return the merged tree.
The rule for merging is that if two nodes overlap, then put the value sum of
both nodes to the new value of merged node. Otherwise, the NOT null node
will be used as the node of new tree.
"""


class Node:
    """
    A binary node has value variable and pointers to its left and right node.
    """

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def merge_two_binary_trees(tree1: Node, tree2: Node) -> Node:
    """
    Returns root node of the merged tree.
    """
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value = tree1.value + tree2.value
    tree1.left = merge_two_binary_trees(tree1.left, tree2.left)
    tree1.right = merge_two_binary_trees(tree1.right, tree2.right)
    return tree1


def print_preorder(root: Node) -> None:
    """
    Print pre-order traversal of the tree.

    >>> root = Node(1)
    >>> root.left = Node(2)
    >>> root.right = Node(3)
    >>> print_preorder(root)
    1
    2
    3
    >>> print_preorder(root.right)
    3
    """
    if root:
        print(root.value)
        print_preorder(root.left)
        print_preorder(root.right)


def main() -> None:
    """
    Main function for testing.
    """
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)
    tree1.left.left = Node(4)

    tree2 = Node(2)
    tree2.left = Node(4)
    tree2.right = Node(6)
    tree2.left.right = Node(9)
    tree2.right.right = Node(5)

    print("Tree1 is: ")
    print_preorder(tree1)
    print("Tree2 is: ")
    print_preorder(tree2)
    merged_tree = merge_two_binary_trees(tree1, tree2)
    print("Merged Tree is: ")
    print_preorder(merged_tree)


if __name__ == "__main__":
    main()