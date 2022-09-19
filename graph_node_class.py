from typing import List


class GraphNode:

    def __init__(self, val=0, adjacent=None, visited: bool = False):
        if adjacent is None:
            adjacent = []
        self.val = val
        self.adjacent = adjacent
        self.visited = visited
