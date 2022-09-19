import math
import time
from typing import List


class Solution:

    def binary_search_arr(self, arr: List[int], target: int) -> bool:
        arr_slice = arr

        while len(arr_slice) > 0:
            mid = math.floor((len(arr_slice) - 1) / 2)

            if arr_slice[mid] < target:
                arr_slice = arr_slice[mid + 1:]
            elif arr_slice[mid] > target:
                arr_slice = arr_slice[:mid]
            else:
                return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = 0

        while row_idx < len(matrix) - 1:
            first_int = matrix[row_idx][0]

            if first_int == target:
                return True

            if first_int < target < matrix[row_idx + 1][0]:
                break

            row_idx += 1

        return self.binary_search_arr(matrix[row_idx], target)


m = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.searchMatrix(m, 3))
    print(sol.searchMatrix(m, 16))
    print(sol.searchMatrix(m, 15))
    print("----%s seconds----" % (time.time() - start_time))
