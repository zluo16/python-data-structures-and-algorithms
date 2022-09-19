from typing import List


nums_list = [1, 2, 3, 4, 5]


def log_all_pairs(nums: List) -> None:
    for i, n in enumerate(nums):
        for j in range(i, len(nums)):
            print(str(n) + " " + str(nums[j]))


log_all_pairs(nums_list)
