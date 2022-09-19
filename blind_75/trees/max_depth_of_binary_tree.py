from typing import Optional

from tree_node_class import TreeNode


class Solution:

    def __init__(self):
        self.max_depth = 0

    def max_depth(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.max_depth

    def dfs(self, root: Optional[TreeNode], depth: Optional[int] = 0) -> None:
        if root is None:
            if depth > self.max_depth:
                self.max_depth = depth
            return

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
