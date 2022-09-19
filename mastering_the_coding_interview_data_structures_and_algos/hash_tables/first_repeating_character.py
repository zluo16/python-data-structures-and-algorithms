# $Google Question
# $Given an array = [2,5,1,2,3,5,1,2,4]:
# $It should return 2

# $Given an array = [2,1,1,2,3,5,1,2,4]:
# $It should return 1

# $Given an array = [2,3,4,5]:
# $It should return undefined


def first_repeating_character(arr):
    hash_map = {}

    for char in arr:
        if char in hash_map:
            return char
        hash_map[char] = True

    return None


a1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
a2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
a3 = [2, 3, 4, 5]


print(first_repeating_character(a1))
print(first_repeating_character(a2))
print(first_repeating_character(a3))
