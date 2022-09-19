def unique_paths(m: int, n: int):
    row = [1] * n

    for i in range(0, m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row

    return row[0]


print(unique_paths(3, 7))
# unique_paths(3, 7)
