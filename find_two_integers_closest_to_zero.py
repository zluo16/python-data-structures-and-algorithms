import time
from typing import List, Tuple


def find_closest_to_zero(nums: List[int]) -> Tuple[int, int]:
    closest_to_zero = None

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if closest_to_zero is None:
                closest_to_zero = (nums[i], nums[j])
            else:
                abs_sum = abs(nums[i] + nums[j])
                if abs_sum < abs(closest_to_zero[0] + closest_to_zero[1]):
                    closest_to_zero = (nums[i], nums[j])

    return closest_to_zero


def find_closest_to_zero_opt(nums: List[int]) -> Tuple[int, int]:
    ns = sorted(nums)
    closest_to_zero = (nums[0], nums[len(nums) - 1])

    left = 1
    right = len(ns) - 2

    while left < right:
        abs_sum = abs(nums[left] + nums[right])
        if abs_sum < abs(closest_to_zero[0] + closest_to_zero[1]):
            closest_to_zero = (nums[left], nums[right])

        left += 1
        right -= 1

    return closest_to_zero


a1 = [1, -2, -3, 2, -4]
a2 = [1, -3, -3, 2, -4]

if __name__ == '__main__':
    start_time = time.time()
    # print(find_closest_to_zero(a1))
    # print(find_closest_to_zero(a2))
    print(find_closest_to_zero_opt(a1))
    print(find_closest_to_zero_opt(a2))
    print("----%s seconds----" % (time.time() - start_time))
