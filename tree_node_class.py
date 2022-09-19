from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_array(array: List[int]) -> TreeNode:
    return create_minimal_bst(array, 0, len(array) - 1)


def create_minimal_bst(array: List[int], start: int, end: int) -> Optional[TreeNode]:
    if end < start:
        return None

    mid_idx = int((start + end) / 2)
    node = TreeNode(array[mid_idx])
    node.left = create_minimal_bst(array, start, mid_idx - 1)
    node.right = create_minimal_bst(array, mid_idx + 1, end)
    return node


nums = [3, 5, 7, 9, 10, 18, 20]


tree_to_test = create_tree_from_array(nums)
