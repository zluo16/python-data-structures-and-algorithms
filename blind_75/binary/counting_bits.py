import ctypes
import time
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            c_num = ctypes.c_ulong(i)
            bin_n = bin(c_num.value)
            bits = sum([int(c) for c in bin_n if c == '1'])
            ans.append(bits)

        return ans


if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.countBits(5))
    print(sol.countBits(11))
    print(sol.countBits(128))
    print("----%s seconds----" % (time.time() - start_time))
