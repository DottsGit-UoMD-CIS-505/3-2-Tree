"""
Author: Nicholas Butzke
"""


class Node:
    def __init__(self, keys, parent=None):
        self.keys: list = keys
        self.parent: Node = parent
        self.children = list()

    def is_leaf(self):
        return len(self.children) == 0


def traverse_tree(node: Node):
    if node.is_leaf():
        for key in node.keys:
            print(key)
    else:
        traverse_tree(node.children[0])
        print(str(node.keys[0]))
        traverse_tree(node.children[1])
        if len(node.keys) == 2:
            print(str(node.keys[1]))
            traverse_tree(node.children[2])
