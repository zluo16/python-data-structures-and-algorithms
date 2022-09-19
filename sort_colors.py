import time
from typing import List


class Solution:

    def swap(self, nums: List[int], idx_1: int, idx_2: int) -> None:
        temp = nums[idx_1]
        nums[idx_1] = nums[idx_2]
        nums[idx_2] = temp

    def partition(self, nums: List[int], pivot: int, left: int, right: int) -> int:
        piv_val = nums[pivot]
        part_i = left

        for i in range(left, right):
            if nums[i] < piv_val:
                self.swap(nums, i, part_i)
                part_i += 1

        self.swap(nums, right, part_i)
        return part_i

    def quicksort(self, nums: List[int], left: int, right: int) -> List[int]:
        if left < right:
            partition_idx = self.partition(nums, right, left, right)

            self.quicksort(nums, left, partition_idx - 1)
            self.quicksort(nums, partition_idx + 1, right)

        return nums

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln_arr = len(nums)
        self.quicksort(nums, 0, ln_arr - 1)


n1 = [2, 0, 2, 1, 1, 0]
n2 = [2, 0, 1]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    sol.sortColors(n1)
    sol.sortColors(n2)
    print(n1)
    print(n2)
    print("----%s seconds----" % (time.time() - start_time))
