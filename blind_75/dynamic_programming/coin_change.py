import time
from typing import List, Optional


class Solution:

    def coin_change(self, coins: List[int], amount: int) -> int:
        coins.sort()
        returned_coins = []
        amount_req = amount

        for i in range(len(coins) - 1, -1, -1):
            while amount_req >= coins[i]:
                returned_coins.append(coins[i])
                amount_req -= coins[i]

        if amount_req != 0:
            return -1

        return len(returned_coins)

    def coin_change_dfs(self, coins: List[int], amount: int, count: Optional[int] = 0) -> int:
        if amount == 0:
            return count

        if amount < 0:
            return -1

        min_count = None

        for c in coins:
            temp_count = self.coin_change_dfs(coins, amount - c, count + 1)
            if min_count is None and temp_count != -1:
                min_count = temp_count
            elif temp_count != -1:
                min_count = min(min_count, temp_count)

        if min_count:
            return min_count
        else:
            return -1

    def coin_change_opt(self, coins: List[int], amount: int) -> int:
        amount_arr = [amount + 1] * (amount + 1)
        amount_arr[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    amount_arr[i] = min(amount_arr[i], amount_arr[i - c] + 1)

        if amount_arr[amount] != amount + 1:
            return amount_arr[amount]
        else:
            return -1


c1 = [1, 2, 5]
c2 = [1, 3, 4, 5]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    # print(sol.coin_change_opt(c1, 11))
    # print(sol.coin_change_opt(c2, 7))
    # print(sol.coin_change_dfs(c1, 11))
    # print(sol.coin_change_dfs(c2, 7))
    print(sol.coin_change_opt(c1, 100))
    # print(sol.coin_change(c1, 100))
    print("----%s seconds----" % (time.time() - start_time))
