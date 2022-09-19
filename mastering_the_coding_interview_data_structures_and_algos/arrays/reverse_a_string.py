from math import floor

string = 'Hi my name is Mike'


def reverse_brute(s):
    reversed_s_arr = []

    for i in range(len(s) - 1, -1, -1):
        reversed_s_arr.append(s[i])

    return ''.join(reversed_s_arr)


print(reverse_brute(string))


def reverse(s):
    s_arr = [*s]

    for i in range(0, floor((len(s_arr) - 1) / 2)):
        j = len(s_arr) - 1 - i
        start = s_arr[i]
        end = s_arr[j]
        s_arr[i] = end
        s_arr[j] = start

    return ''.join(s_arr)


print(reverse(string))
