from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jumps = nums[0]

        i = 0
        while i < len(nums) - 1:
            current_max_jumps = 0
            jumps_used = 0
            for j in range(i + 1, (i + current_jumps) + 1):
                if j == len(nums) - 1:
                    jumps_used = len(nums) - 1
                elif j < len(nums) and nums[j] + j > current_max_jumps:
                    current_max_jumps = nums[j]
                    jumps_used += 1

            jumps += 1
            current_jumps = current_max_jumps
            i += jumps_used

        return jumps


sol = Solution()


# for i in range(1, 2):
#     print(i)


print(sol.jump([1, 3, 2]))
print(sol.jump([2, 3, 1]))
