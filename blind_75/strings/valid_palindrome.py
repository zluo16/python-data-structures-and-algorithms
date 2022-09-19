import math
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = re.sub(r'[^a-zA-Z0-9]', '', s)
        s_lower = s_alpha.lower()

        mid_idx = math.ceil(len(s_lower) / 2)

        for i in range(mid_idx, len(s_lower)):
            left = len(s_lower) - 1 - i
            if s_lower[i] != s_lower[left]:
                return False

        return True
