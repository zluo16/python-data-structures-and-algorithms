def char_to_bits(string):
    if len(string) == 0:
        return ''

    bits_arr = []
    prev_char = string[0]
    char_count = 1

    for i in range(1, len(string)):
        if string[i] == prev_char:
            char_count += 1
        else:
            bits_arr.append(char_count)
            bits_arr.append(prev_char)
            prev_char = string[i]
            char_count = 1

    bits_arr.append(char_count)
    bits_arr.append(prev_char)

    string_bits_arr = [
        str(item) for item in bits_arr
    ]

    return ''.join(string_bits_arr)


s = 'aaaabbbcccca'
print(char_to_bits(s))

s1 = 'abbbbccccb'
print(char_to_bits(s1))

s2 = 'aaaabbbccccaaaaa'
print(char_to_bits(s2))

s3 = 'a'
print(char_to_bits(s3))
