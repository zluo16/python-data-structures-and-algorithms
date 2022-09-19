def length_of_longest_sub(string: str) -> int:
    char_set = set()
    left = 0
    result = 0

    # Sliding window implementation
    for right in range(0, len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left += 1
        char_set.add(string[right])
        result = max(result, right - left + 1)

    return result


print(length_of_longest_sub('abcabcbbdd'))
