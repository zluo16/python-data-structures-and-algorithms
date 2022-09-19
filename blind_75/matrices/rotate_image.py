import math
import time
from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sq_len = len(matrix[0])
        mid = math.floor((sq_len - 1) / 2)
        level_idx = 0

        while level_idx <= mid:
            for i in range(level_idx, sq_len - 1 - level_idx):
                inverse_lev = sq_len - 1 - level_idx
                inverse_idx = sq_len - 1 - i

                right = matrix[i][inverse_lev]
                top = matrix[level_idx][i]
                bottom = matrix[inverse_lev][inverse_idx]
                left = matrix[inverse_idx][level_idx]

                matrix[i][inverse_lev] = top
                matrix[inverse_lev][inverse_idx] = right
                matrix[inverse_idx][level_idx] = bottom
                matrix[level_idx][i] = left

            level_idx += 1


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    sol.rotate(m1)
    sol.rotate(m2)
    print(m1)
    print(m2)
    print("----%s seconds----" % (time.time() - start_time))
