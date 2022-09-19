from typing import List

a1 = [1, 2, 4, 5]
a2 = [1, 2, 4, 4]


def pair_sum_exists(arr: List[int], n: int) -> bool:
    int_map = {}
    for num in arr:
        if num in int_map:
            int_map[num] += 1
        else:
            int_map[num] = 1

    for num in arr:
        diff = n - num
        if diff in int_map:
            if diff == num:
                return True if int_map[num] > 1 else False
            else:
                return True

    return False


print(pair_sum_exists(a1, 8))
print(pair_sum_exists(a2, 8))
print(pair_sum_exists(a1, 9))
