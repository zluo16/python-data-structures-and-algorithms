class Solution:

    def climb_stairs(self, n: int) -> int:
        cache = {0: 0}

        def dfs(n: int, val: int) -> None:
            if n <= 0:
                if n == 0:
                    cache[0] += 1
                return None

            dfs(n - 1, val)
            dfs(n - 2, val)

        dfs(n, n)
        return cache[0]
