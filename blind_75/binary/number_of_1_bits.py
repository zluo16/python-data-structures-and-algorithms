import ctypes
import time


class Solution:
    def hammingWeight(self, n: int) -> int:
        ct_n = ctypes.c_ulong(n)
        unsigned_n = bin(ct_n.value)
        b_count = 0

        for char in unsigned_n:
            if char == '1':
                b_count += 1

        return b_count


if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.hammingWeight(11))
    print(sol.hammingWeight(128))
    print(sol.hammingWeight(0))
    print("----%s seconds----" % (time.time() - start_time))
