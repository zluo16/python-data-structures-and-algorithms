import collections
from typing import Optional, List


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        tree_node = TreeNode(val)

        if self.root is None:
            self.root = tree_node
            return self.root

        root = self.root
        while root:
            if val < root.val:
                if root.left is None:
                    root.left = tree_node
                    return self.root
                root = root.left
            else:
                if root.right is None:
                    root.right = tree_node
                    return self.root
                root = root.right

    def lookup(self, n):
        if self.root is None:
            return None

        root = self.root
        while root:
            if root.val == n:
                return root

            if root.val > n:
                root = root.left
            else:
                root = root.right

        return None

    @staticmethod
    def dfs(root: Optional[TreeNode] = None, visited: Optional[List[TreeNode]] = None) -> Optional[TreeNode]:
        vis = visited or []

        if root is None:
            return None

        print(root.val)

        vis.append(root.val)

        BinarySearchTree.dfs(root.left, vis)
        BinarySearchTree.dfs(root.right, vis)

    def bfs(self, level):
        BinarySearchTree._print_current_level(self.root, level)

    @staticmethod
    def _print_current_level(root, level):
        if root is None:
            return None

        if level == 1:
            print(root.val)
        elif level > 1:
            BinarySearchTree._print_current_level(root.left, level - 1)
            BinarySearchTree._print_current_level(root.right, level - 1)

    def breadth_first_search(self):
        root = self.root
        li = []
        queue = [root]

        while queue:
            root = queue.pop(0)
            li.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        return li

    def dfs_in_order(self, root, li):
        if root is not None:
            self.dfs_in_order(root.left, li)
            li.append(root.val)
            self.dfs_in_order(root.right, li)
        return li

    def dfs_pre_order(self, root, li):
        if root is not None:
            li.append(root.val)
            self.dfs_in_order(root.left, li)
            self.dfs_in_order(root.right, li)
        return li

    def dfs_post_order(self, root, li):
        if root is not None:
            self.dfs_in_order(root.left, li)
            self.dfs_in_order(root.right, li)
            li.append(root.val)
        return li

    def print_left_side(self) -> List[int]:
        root = self.root
        q = collections.deque()
        levels = []

        if root:
            q.append(root)

        while q:
            level = []
            for i in range(0, len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                levels.append(level)

        return [level[0] for level in levels]


def print_tree(root: Optional[TreeNode]) -> None:
    if root is not None:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)


search_tree = BinarySearchTree()

search_tree.insert(9)
search_tree.insert(4)
search_tree.insert(6)
search_tree.insert(20)
search_tree.insert(170)
search_tree.insert(15)
search_tree.insert(1)

#       9
#    4     20
# 2    6 15   170

# print_tree(search_tree.root)
# n = search_tree.lookup(6)
# if n:
#     print(n.val)
# else:
#     print("Couldn't find the node..")

# search_tree.bfs(3)
# print(search_tree.breadth_first_search())
# print(search_tree.dfs_in_order(search_tree.root, []))
# print(search_tree.dfs_pre_order(search_tree.root, []))
# print(search_tree.dfs_post_order(search_tree.root, []))
print(search_tree.print_left_side())
