import collections
import time
import math


class Solution:
    def is_palindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        mid_idx = math.ceil(len(s) / 2)

        for i in range(mid_idx, len(s)):
            left = len(s) - 1 - i
            if s[i] != s[left]:
                return False

        return True

    def should_replace_longest(self, s: str, curr_long: str) -> bool:
        return self.is_palindrome(s) and len(curr_long) < len(s)

    def first_pos(self, s: str, start: int, end: int) -> int:
        for i in range(start, end + 1):
            if 97 <= ord(s[i]) <= 122:
                return i
        return -1

    def last_pos(self, s: str, start: int, end: int) -> int:
        for i in range(start, end - 1, -1):
            if 97 <= ord(s[i]) <= 122:
                return i
        return -1

    def is_palindrome_opt(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        res = True

        for i in range(0, len(s)):
            first = self.first_pos(s, first, last)
            last = self.last_pos(s, last, first)

            if last < 0 or first < 0:
                break

            if s[first] == s[last]:
                first += 1
                last -= 1
                continue

            res = False
            break

        return res

    def longest_palindrome_opt(self, s: str) -> str:
        if len(s) < 2:
            return s

        q = collections.deque()
        left = 0

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        long_pal = ''

        for i in range(0, len(s) - 1):
            right = i
            left = i

            while left >= 0 or right < len(s):
                if self.should_replace_longest(s[left:right + 1], long_pal):
                    long_pal = s[left:right + 1]

                right += 1

                if self.should_replace_longest(s[left:right + 1], long_pal):
                    long_pal = s[left:right + 1]

                left -= 1

        return long_pal


sol = Solution()

really_long_string = (
    "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"
)

start_time = time.time()
print(sol.longestPalindrome(really_long_string))
# print(sol.is_palindrome_opt('gykrkyg'))
print("----%s seconds----" % (time.time() - start_time))
