import collections
import time
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [
            [0 for i in range(n)]
            for j in range(n)
        ]
        nums_q = collections.deque(
            [i for i in range(1, (n * n) + 1)]
        )

        left, right = 0, n
        top, bottom = 0, n

        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = nums_q.popleft()

            top += 1

            for i in range(top, bottom):
                matrix[i][right - 1] = nums_q.popleft()

            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = nums_q.popleft()

            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = nums_q.popleft()

            left += 1

        return matrix


if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.generateMatrix(3))
    print(sol.generateMatrix(4))
    print("----%s seconds----" % (time.time() - start_time))
