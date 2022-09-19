# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacci_recursive(idx):
    if idx < 2:
        return idx

    return fibonacci_recursive(idx - 2) + fibonacci_recursive(idx - 1)


def fibonacci_iterative(idx):
    arr = [0, 1]
    for n in range(2, idx + 1):
        arr.append(arr[n - 2] + arr[n - 1])

    return arr[idx]


# print(fibonacci_recursive(20))
print(fibonacci_iterative(43))
