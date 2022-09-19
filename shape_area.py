def solution(n):
    if n == 1:
        return n

    hash_map = {1: 1}

    for n in range(2, n + 1):
        to_add = (n * 4) - 4
        hash_map[n] = hash_map[n - 1] + to_add

    return hash_map[n]
