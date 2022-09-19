from typing import List


def check_slice(arr):
    last_idx = len(arr) - 1
    if arr[0] - arr[last_idx] != last_idx:
        return False

    arr_range = range(arr[0], arr[last_idx] - 1, -1)
    return list(arr_range) == arr


def count_decreasing_ratings(ratings: List):
    if len(ratings) < 0:
        return 0

    counts = 0

    for i in range(0, len(ratings)):
        for j in range(i, len(ratings)):
            arr = ratings[i:j + 1]
            if check_slice(arr):
                counts += 1

    return counts


r1 = [4, 3, 5, 4, 3]


print(count_decreasing_ratings(r1))
