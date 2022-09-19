from typing import Optional

from tree_node_class import TreeNode


class Solution:

    def __init__(self):
        self.comp_vals = []

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.dfs(p, q)
        if False in self.comp_vals:
            return False
        else:
            return True

    def dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
        if p is None and q is None:
            self.comp_vals.append(True)
            return
        elif p is None or q is None:
            self.comp_vals.append(False)
            return

        if p.val == q.val:
            self.comp_vals.append(True)
        else:
            self.comp_vals.append(False)
            return

        self.dfs(p.left, q.left)
        self.dfs(p.right, q.right)
