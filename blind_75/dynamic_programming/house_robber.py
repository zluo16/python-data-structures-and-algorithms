import time
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp

        return r2


n1 = [1, 2, 3, 1]
n2 = [2, 7, 9, 3, 1]
n3 = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
      185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.rob(n1))
    print(sol.rob(n2))
    print(sol.rob(n3))
    print("----%s seconds----" % (time.time() - start_time))
