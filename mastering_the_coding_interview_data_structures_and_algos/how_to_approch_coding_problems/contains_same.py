array1 = ['w', 'x', 'y', 'z']
array2 = ['a', 'b', 'z']

array3 = ['w', 'x', 'y', 'z']
array4 = ['a', 'b', 'c']


def contains_same(a1, a2):
    hash_map = {}
    for i, item in enumerate(a1):
        if item not in hash_map:
            hash_map[item] = i

    for letter in a2:
        if letter in hash_map.keys():
            return True

    return False


print(contains_same(array1, array2))
print(contains_same(array3, array4))
