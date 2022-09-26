import time
from typing import List


class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.is_word = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=len)

        trie = Trie()

        for s in sorted_strs:
            if s == '':
                return ''
            trie.add_word(s)

        common_pre = ''
        prev_is_word = False

        while len(trie.children.keys()) == 1 and not prev_is_word:
            c = list(trie.children.keys())[0]
            common_pre += c
            new_trie = trie.children[c]
            prev_is_word = new_trie.is_word
            trie = new_trie

        return common_pre


s1 = ["flower", "flow", "flight"]
s2 = ["dog", "racecar", "car"]
s3 = ["ab", "a"]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.longestCommonPrefix(s1))
    print(sol.longestCommonPrefix(s2))
    print(sol.longestCommonPrefix(s3))
    print("----%s seconds----" % (time.time() - start_time))
