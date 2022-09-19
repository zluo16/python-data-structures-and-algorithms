import time
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)

        return max_sum


n1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n2 = [5, 4, -1, 7, 8]
n3 = [1]


if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.maxSubArray(n1))
    print(sol.maxSubArray(n2))
    print(sol.maxSubArray(n3))
    print("----%s seconds----" % (time.time() - start_time))
