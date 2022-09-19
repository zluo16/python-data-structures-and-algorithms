a1 = [0, 3, 4, 31]
a2 = [4, 6, 30, 32, 33, 34]


def merge_sorted(arr1, arr2):
    merged_arr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i == len(arr1):
            merged_arr.append(arr2[j])
            j += 1
        elif j == len(arr2):
            merged_arr.append(arr1[i])
            i += 1
        elif arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    return merged_arr


def merge_sorted_clean(arr1, arr2):
    merged_arr = []
    item1 = arr1[0] if len(arr1) > 0 else None
    item2 = arr2[0] if len(arr2) > 0 else None

    i = 0
    j = 0
    while item1 or item2:
        if item1 is not None and item1 < item2:
            merged_arr.append(item1)
            i += 1
            item1 = arr1[i] if len(arr1) > i else None
        else:
            merged_arr.append(item2)
            j += 1
            item2 = arr2[j] if len(arr2) > j else None

    return merged_arr


print(merge_sorted(a1, a2))
print(merge_sorted_clean(a1, a2))
