from typing import Optional

from tree_node_class import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_vals = []

        def dfs(node):
            if node is not None:
                dfs(node.left)
                inorder_vals.append(node.val)
                dfs(node.right)

        dfs(root)

        if k > len(inorder_vals):
            return -1

        return inorder_vals[k - 1]
