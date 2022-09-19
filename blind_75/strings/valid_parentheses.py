import collections


class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        close_parens = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        if s[0] in close_parens:
            return False

        paren_stack = collections.deque()

        paren_map = {}
        for i, p in enumerate(s):
            if p in paren_map:
                paren_map[p].append(i)
            else:
                paren_map[p] = [i]

            if p in open_parens:
                paren_stack.append(p)
            elif p in close_parens:
                last_stack_idx = len(paren_stack) - 1
                if len(paren_stack) > 0 and paren_stack[last_stack_idx] == close_parens[p]:
                    paren_stack.pop()
                elif len(paren_stack) > 0 and paren_stack[last_stack_idx] != close_parens[p]:
                    return False

        if len(paren_stack) > 0:
            return False

        for i, open_par in enumerate(open_parens.keys()):
            paren_stack = collections.deque()

            close_par = open_parens[open_par]
            if open_par in paren_map:
                if close_par not in paren_map:
                    return False

                if len(paren_map[open_par]) != len(paren_map[close_par]):
                    return False

                for i in range(0, len(paren_map[open_par])):
                    if paren_map[open_par][i] > paren_map[close_par][i]:
                        return False

        return True


class SolutionOptimized:
    def isValid(self, s: str) -> bool:
        open_parens = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        close_parens = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        paren_stack = collections.deque()

        for p in s:
            if p in open_parens:
                paren_stack.append(p)
            elif p in close_parens:
                if len(paren_stack) == 0:
                    return False
                last_idx = len(paren_stack) - 1
                if paren_stack[last_idx] != close_parens[p]:
                    return False
                paren_stack.pop()

        return len(paren_stack) == 0
