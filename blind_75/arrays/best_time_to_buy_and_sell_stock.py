import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min = None
        max_profit = 0
        for i in range(1, len(prices)):
            if last_min is None:
                last_min = prices[i - 1]
            else:
                last_min = min(last_min, prices[i - 1])
            max_profit = max(prices[i] - last_min, max_profit)
        return max_profit


a1 = [7, 1, 5, 3, 6, 4]
a2 = [7, 6, 4, 3, 1]
a3 = [1, 2]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.maxProfit(a1))
    print(sol.maxProfit(a2))
    print(sol.maxProfit(a3))
    print("----%s seconds----" % (time.time() - start_time))
