def bubble_sort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - 1):
            if arr[j] > arr[j + 1]:
                leader = arr[j]
                follower = arr[j + 1]
                arr[j] = follower
                arr[j + 1] = leader

    return arr


a1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(bubble_sort(a1))
