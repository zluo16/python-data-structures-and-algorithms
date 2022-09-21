import time
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        last_idx = len(nums) - 1

        prod_in_order = {0: nums[0]}
        for i in range(1, len(nums)):
            prod_in_order[i] = nums[i] * prod_in_order[i - 1]

        prod_reverse = {last_idx: nums[last_idx]}
        for i in range(len(nums) - 2, -1, -1):
            prod_reverse[i] = nums[i] * prod_reverse[i + 1]

        prod_arr = [prod_reverse[1]]

        for i in range(1, last_idx):
            prod = prod_reverse[i + 1] * prod_in_order[i - 1]
            prod_arr.append(prod)

        prod_arr.append(prod_in_order[last_idx - 1])
        return prod_arr


n1 = [1, 2, 3, 4]
n2 = [-1, 1, 0, -3, 3]
n3 = [4, 3, 2, 1, 2]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.productExceptSelf(n1))
    print(sol.productExceptSelf(n2))
    print(sol.productExceptSelf(n3))
    print("----%s seconds----" % (time.time() - start_time))
