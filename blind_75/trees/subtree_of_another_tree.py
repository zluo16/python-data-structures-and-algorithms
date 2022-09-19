from typing import Optional

from tree_node_class import TreeNode


class Solution:

    def __init__(self):
        self.same_tree_search = []
        self.actual_sub_node = None

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.dfs(root, subRoot.val)
        return self.same_tree(self.actual_sub_node, subRoot)

    def dfs(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            self.actual_sub_node = root

        self.dfs(root.left, val)
        self.dfs(root.right, val)

    def same_tree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_same_tree_dfs(root, subRoot)
        if False in self.same_tree_search:
            return False
        else:
            return True

    def is_same_tree_dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> None:
        if root is None and subRoot is None:
            self.same_tree_search.append(True)
            return
        elif root is None or subRoot is None:
            self.same_tree_search.append(False)
            return

        if root.val == subRoot.val:
            self.same_tree_search.append(True)
        else:
            self.same_tree_search.append(False)

        self.is_same_tree_dfs(root.left, subRoot.left)
        self.is_same_tree_dfs(root.right, subRoot.right)
