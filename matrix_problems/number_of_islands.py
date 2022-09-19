from typing import List


class Solution:

    def __init__(self):
        self.x_vex = [0, 1, 0, -1]
        self.y_vex = [-1, 0, 1, 0]

    def is_valid_cell(self, row: int, col: int, matrix: List[List[bool]]) -> bool:
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
            return False

        if matrix[row][col]:
            return False

        return True

    def dfs_util(self, row: int, col: int, matrix: List[List[bool]]) -> None:
        if not self.is_valid_cell(row, col, matrix):
            return

        matrix[row][col] = True

        for i in range(4):
            r = row + self.x_vex[i]
            c = col + self.y_vex[i]
            self.dfs_util(r, c, matrix)

    def numIslands(self, grid: List[List[str]]) -> int:

        map_matrix = [
            [False if cell == '1' else True for cell in row]
            for row in grid
        ]

        island_count = 0

        for x in range(len(map_matrix)):
            for y in range(len(map_matrix[x])):
                if not map_matrix[x][y]:
                    self.dfs_util(x, y, map_matrix)
                    island_count += 1

        return island_count


mat_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

mat_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

sol = Solution()

print(sol.numIslands(mat_1))
print(sol.numIslands(mat_2))
