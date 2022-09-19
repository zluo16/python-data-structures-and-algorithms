import time
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums_sorted = sorted(nums)

        for i, n in enumerate(nums_sorted):
            if i > 0 and n == nums_sorted[i - 1]:
                continue

            left = i + 1
            right = len(nums_sorted) - 1

            while left < right:
                if left > i + 1 and nums_sorted[left] == nums_sorted[left - 1]:
                    left += 1
                    continue

                three_sum = n + nums_sorted[left] + nums_sorted[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    triplets.append([n, nums_sorted[left], nums_sorted[right]])
                    left += 1

        return triplets


a1 = [-1, 0, 1, 2, -1, -4]
a2 = [0, 1, 1]
a3 = [0, 0, 0]
a4 = [-3, 3, 4, -3, 1, 2]
a5 = [0, 0, 0, 0]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.threeSum(a1))
    print(sol.threeSum(a2))
    print(sol.threeSum(a3))
    print(sol.threeSum(a4))
    print(sol.threeSum(a5))
    print("----%s seconds----" % (time.time() - start_time))
