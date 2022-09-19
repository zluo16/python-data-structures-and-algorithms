def find_factorial_recursive(num):
    if num == 1:
        return 1
    return num * find_factorial_recursive(num - 1)


def find_factorial_iterative(num):
    base = num
    for n in range(num - 1, 0, -1):
        base = base * n
    return base


print(find_factorial_recursive(5))
print(find_factorial_iterative(5))
