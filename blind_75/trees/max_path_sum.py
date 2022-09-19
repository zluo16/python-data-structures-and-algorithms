from typing import Optional

from tree_node_class import TreeNode


class Solution:

    def __init__(self):
        self.max_path = 0

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        self.max_path = root.val
        self.dfs(root)
        return self.max_path

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_max = self.dfs(root.left)
        right_max = self.dfs(root.right)

        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        self.max_path = max(root.val + left_max + right_max, self.max_path)

        return root.val + max(left_max, right_max)
