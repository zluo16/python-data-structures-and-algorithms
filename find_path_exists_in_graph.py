from typing import List, Optional


class Solution:

    def __init__(self) -> None:
        self.hash_map = {}

    def valid_path(self, edges: List[List[int]], source: int, destination: int) -> bool:
        self._add_edges_to_map(edges)

        visited = []
        queue = []

        visited.append(source)
        queue.append(source)

        while queue:
            n = queue.pop()
            if n == destination:
                return True

            for neighbor in self.hash_map[n]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

        return False

    def valid_path_dfs(self, edges: List[List[int]], source: int, destination: int) -> bool:
        self._add_edges_to_map(edges)
        return self._dfs(source, destination, [])

    def _dfs(self, source: int, destination: int, visited: List[int]) -> bool:
        if source == destination:
            return True

        visited.append(source)

        for n in self.hash_map[source]:
            if n not in visited:
                return self._dfs(n, destination, visited)

        return False

    def _add_edges_to_map(self, edges: List[List[int]]) -> None:
        for edge in edges:
            if edge[0] not in self.hash_map:
                self.hash_map[edge[0]] = [edge[1]]
            else:
                self.hash_map[edge[0]].append(edge[1])

            if edge[1] not in self.hash_map:
                self.hash_map[edge[1]] = [edge[0]]
            else:
                self.hash_map[edge[1]].append(edge[0])


path_graph = [[0, 1], [1, 2], [2, 0]]
no_path_graph = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]

sol = Solution()


print(sol.valid_path(path_graph, 0, 2))
print(sol.valid_path(no_path_graph, 0, 5))


sol = Solution()


print(sol.valid_path_dfs(path_graph, 0, 2))
print(sol.valid_path_dfs(no_path_graph, 0, 5))
