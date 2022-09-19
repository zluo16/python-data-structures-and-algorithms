from typing import List


def swap(nums: List[int], idx_1: int, idx_2: int) -> None:
    temp = nums[idx_1]
    nums[idx_1] = nums[idx_2]
    nums[idx_2] = temp


def partition(nums: List[int], pivot: int, left: int, right: int) -> int:
    piv_val = nums[pivot]
    part_i = left

    for i in range(left, right):
        if nums[i] < piv_val:
            swap(nums, i, part_i)
            part_i += 1

    swap(nums, right, part_i)
    return part_i


def quicksort(nums: List[int], left: int, right: int) -> List[int]:
    if left < right:
        partition_idx = partition(nums, right, left, right)

        quicksort(nums, left, partition_idx - 1)
        quicksort(nums, partition_idx + 1, right)

    return nums
