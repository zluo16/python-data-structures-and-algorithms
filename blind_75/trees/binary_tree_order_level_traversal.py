import collections
from typing import Optional, List

from tree_node_class import TreeNode


class Solution:

    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        queue = collections.deque()

        if root is not None:
            queue.append(root)

        while queue:
            level = []
            for i in range(0, len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                levels.append(level)

        return levels
