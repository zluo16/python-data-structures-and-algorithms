from typing import Optional

from tree_node_class import TreeNode


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            left = root.left
            right = root.right

            root.left = right
            root.right = left

            self.invert_tree(root.left)
            self.invert_tree(root.right)
        return root
