import math


class Solution:
    def reverse(self, x: int) -> int:
        int_str_arr = [*str(x)]
        mid = math.floor(len(int_str_arr) / 2)

        for i in range(mid - 1, -1, -1):
            j = len(int_str_arr) - 1 - i
            left = int_str_arr[i]
            right = int_str_arr[j]

            int_str_arr[j] = left
            int_str_arr[i] = right

        if int_str_arr[len(int_str_arr) - 1] == '-':
            abs_str = ''.join(int_str_arr[:len(int_str_arr) - 1])
            int_str = '-' + abs_str
        else:
            int_str = ''.join(int_str_arr)

        if int(int_str) > 2 ** 31 or int(int_str) < -2 ** 31:
            return 0

        return int(int_str)
