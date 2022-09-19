import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)

        small = None

        for i in range(math.floor((len(nums)) / 2)):
            j = len(nums) - 1 - i

            if small is None or small > nums[i]:
                small = nums[i]

            if small is None or small > nums[j]:
                small = nums[j]

            if nums[i] > nums[i + 1]:
                return nums[i + 1]
            elif nums[j] < nums[j - 1]:
                return nums[j]

        return small
