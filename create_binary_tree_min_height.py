import math
from typing import List, Optional

from tree_node_class import TreeNode


def create_tree_from_array(array: List[int]) -> TreeNode:
    return create_minimal_bst(array, 0, len(array) - 1)


def create_minimal_bst(array: List[int], start: int, end: int) -> Optional[TreeNode]:
    if end < start:
        return None

    mid_idx = math.floor((start + end) / 2)
    node = TreeNode(array[mid_idx])
    node.left = create_minimal_bst(array, start, mid_idx - 1)
    node.right = create_minimal_bst(array, mid_idx + 1, end)
    return node


nums = [3, 5, 7, 9, 10, 18, 20, 21]


tree = create_tree_from_array(nums)


def in_order_traversal(root: Optional[TreeNode]) -> None:
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)


in_order_traversal(tree)


def pre_order_traversal(root: Optional[TreeNode]) -> None:
    if root is not None:
        print(root.val)
        in_order_traversal(root.left)
        in_order_traversal(root.right)


# pre_order_traversal(tree)


def post_order_traversal(root: Optional[TreeNode]) -> None:
    if root is not None:
        in_order_traversal(root.left)
        in_order_traversal(root.right)
        print(root.val)


# post_order_traversal(tree)


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    visited = []
    queue = [root]

    while queue:
        root_node = queue.pop(0)
        visited.append(root_node.val)

        if not root_node.left and root_node.right:
            return False
        elif not root_node.right and root_node.left:
            return False

        if root_node.left:
            if root_node.left.val >= root_node.val:
                return False
            queue.append(root_node.left)
        if root_node.right:
            if root_node.right.val <= root_node.val:
                return False
            queue.append(root_node.right)

    return True
