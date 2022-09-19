from typing import List


class Solution:
    def check_anagram(self, string1, string2):
        if len(string1) != len(string2):
            return False

        str_map = {}
        for char in string1:
            if char in str_map:
                str_map[char] += 1
            else:
                str_map[char] = 1

        for char in string2:
            if char in str_map:
                str_map[char] -= 1

        for val in str_map.values():
            if val != 0:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = []
        str_list = strs

        while str_list:
            item = str_list.pop()
            group = [item]
            for s in str_list:
                if self.check_anagram(item, s):
                    group.append(s)
            str_list = [s for s in str_list if s not in group]
            anagram_groups.append(group)

        return anagram_groups
