import math
from typing import List


class Solution:

    def find_pivot_idx(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i + 1
        return -1

    def get_sorted_nums(self, nums: List[int]) -> List[int]:
        pivot_idx = self.find_pivot_idx(nums)
        if pivot_idx == -1:
            return nums

        first_slice = nums[pivot_idx:]
        second_slice = nums[:pivot_idx]

        return first_slice + second_slice

    def search(self, nums: List[int], target: int) -> int:
        num_map = {}
        for i, n in enumerate(nums):
            num_map[n] = i

        sorted_nums = self.get_sorted_nums(nums)

        while len(sorted_nums) > 0:
            mid = math.floor((len(sorted_nums) - 1) / 2)

            if sorted_nums[mid] < target:
                sorted_nums = sorted_nums[mid + 1:]
            elif sorted_nums[mid] > target:
                sorted_nums = sorted_nums[:mid]
            else:
                return num_map[sorted_nums[mid]]

        return -1
