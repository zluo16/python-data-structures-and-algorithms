import collections
from typing import Optional

from tree_node_class import TreeNode


class Solution:
    def bfs_level_count(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()

        if root is not None:
            q.append(root)

        levels = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                levels.append(level)

        return len(levels)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left_height = self.bfs_level_count(root.left)
        right_height = self.bfs_level_count(root.right)

        return abs(left_height - right_height) <= 1
