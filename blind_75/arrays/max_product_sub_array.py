import time
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max(nums)
        curr_prod = 1

        for n in nums:
            if curr_prod == 0:
                curr_prod = 1

            curr_prod = curr_prod * n
            max_prod = max(max_prod, curr_prod)

        return max_prod


n1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n2 = [5, 4, -1, 7, 8]
n3 = [1]
n4 = [2, 3, -2, 4]
n5 = [-2, 0, -1]
n6 = [3, -1, 4]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.maxProduct(n1))
    print(sol.maxProduct(n2))
    print(sol.maxProduct(n3))
    print(sol.maxProduct(n4))
    print(sol.maxProduct(n5))
    print(sol.maxProduct(n6))
    print("----%s seconds----" % (time.time() - start_time))
