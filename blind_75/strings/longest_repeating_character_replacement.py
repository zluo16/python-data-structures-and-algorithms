import time


class Solution:
    def can_replace(self, s: str, k: int) -> bool:
        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1

        for c in s_map.keys():
            if (len(s) - s_map[c]) <= k:
                return True

        return False

    def characterReplacement(self, s: str, k: int) -> int:
        longest_len = 0
        left = 0

        for right in range(1, len(s) + 1):
            sub_str = s[left:right]
            if self.can_replace(sub_str, k):
                longest_len = max(longest_len, len(sub_str))
                continue
            else:
                left += 1

        return longest_len


if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.characterReplacement('ABAB', 2))
    print(sol.characterReplacement('AABABBA', 1))
    print("----%s seconds----" % (time.time() - start_time))
