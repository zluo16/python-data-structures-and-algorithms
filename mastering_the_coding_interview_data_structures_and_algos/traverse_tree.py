from typing import Optional

from tree_node_class import TreeNode, tree_to_test


def print_left_of_tree(root: Optional[TreeNode]):
    if root is not None:
        print(root.val)
        if root.left is not None:
            print_left_of_tree(root.left)
        else:
            print_left_of_tree(root.right)


print(tree_to_test)
print_left_of_tree(tree_to_test)
