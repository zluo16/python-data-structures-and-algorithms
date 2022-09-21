import time
from typing import List


class Solution:

    def set_row_to_zero(self, row: int, matrix: List[List[int]]) -> None:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0

    def set_col_to_zero(self, col: int, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            matrix[i][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_len = len(matrix)
        col_len = len(matrix[0])

        visited_mat = [
            [False for i in range(col_len)]
            for j in range(row_len)
        ]

        zeroes = []

        def dfs_zero_search(row: int, col: int) -> None:
            if row < 0 or col < 0 or row >= row_len or col >= col_len:
                return

            if visited_mat[row][col]:
                return

            visited_mat[row][col] = True

            if matrix[row][col] == 0:
                zeroes.append([row, col])

            col_move = [1, 0, -1, 0]
            row_move = [0, 1, 0, -1]

            for i in range(4):
                new_row = row + row_move[i]
                new_col = col + col_move[i]
                dfs_zero_search(new_row, new_col)

        dfs_zero_search(0, 0)

        for row, col in zeroes:
            self.set_row_to_zero(row, matrix)
            self.set_col_to_zero(col, matrix)


m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    sol.setZeroes(m1)
    sol.setZeroes(m2)
    print(m1)
    print(m2)
    print("----%s seconds----" % (time.time() - start_time))
