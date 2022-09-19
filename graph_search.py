from collections import deque
from typing import Optional

from graph_node_class import GraphNode


def depth_first_search(root: Optional[GraphNode]) -> None:
    if root is None:
        return

    print(root.val)

    root.visited = True

    for n in root.adjacent:
        if not n.visited:
            depth_first_search(n)


def breadth_first_search(root: Optional[GraphNode]) -> None:
    queue = []
    print(root.val)
    root.visited = True
    queue.append(root)

    while queue:
        node = queue.pop()
        for n in node:
            if not n.visited:
                print(n.val)
                n.visited = True
                queue.append(n)
