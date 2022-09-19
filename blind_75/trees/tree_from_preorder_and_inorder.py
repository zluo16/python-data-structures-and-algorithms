import heapq
from typing import List, Optional

from tree_node_class import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


l1 = [1, 3, 2, 7, 5]
heap1 = [-i for i in l1]
heapq.heapify(heap1)
print(heap1)
print(-heapq.heappop(heap1))
