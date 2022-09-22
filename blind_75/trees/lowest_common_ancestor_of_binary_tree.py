from tree_node_class import TreeNode


class Solution:
    def search_util(self, root: TreeNode, val: int) -> bool:
        if root is None:
            return False

        if root.val == val:
            return True

        if root.val < val:
            return self.search_util(root.right, val)
        else:
            return self.search_util(root.left, val)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_is_root = root.val == p.val
        q_is_root = root.val == q.val

        p_in_left = self.search_util(root.left, p.val)
        p_in_right = self.search_util(root.right, p.val)

        q_in_left = self.search_util(root.left, q.val)
        q_in_right = self.search_util(root.right, q.val)

        if (
            (p_in_left and q_in_right)
            or (p_in_right and q_in_left)
            or (p_is_root and q_in_right)
            or (p_is_root and q_in_left)
            or (q_is_root and p_in_right)
            or (q_is_root and p_in_left)
        ):
            return root

        if p_in_left and q_in_left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_in_right and q_in_right:
            return self.lowestCommonAncestor(root.right, p, q)
