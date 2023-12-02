"""
Author: Nicholas Butzke
"""
from tree_class import Node, traverse_tree

root = Node([10, 15])
root.children = [Node([5]), Node([13]), Node([17, 20])]
root.children[0].children = [Node([3]), Node([8, 9])]
root.children[1].children = [Node([11]), Node([14])]
root.children[2].children = [Node([16]), Node([18]), Node([25, 30])]

traverse_tree(root)
