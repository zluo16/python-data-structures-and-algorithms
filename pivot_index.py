from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot_hash = {}

        for i in range(0, len(nums)):
            if i == 0:
                pivot_hash[0] = [0, 0]
            else:
                pivot_hash[i] = [pivot_hash[i - 1][0] + nums[i - 1], 0]

        for j in range(len(nums) - 2, -1, -1):
            pivot_hash[j][1] = nums[j + 1] + pivot_hash[j + 1][1]

        for k in pivot_hash.keys():
            if pivot_hash[k][0] == pivot_hash[k][1]:
                return k

        return -1
