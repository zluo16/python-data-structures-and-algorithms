import time
from typing import List, Set, Tuple


class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

    def add_word(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True


class Solution:

    def is_valid_cell(
        self,
        row: int,
        col: int,
        board: List[List[str]],
        visited: Set[Tuple[int, int]],
        node: TrieNode,
    ) -> bool:
        row_len = len(board[0])
        col_len = len(board)

        if row < 0 or col < 0 or row >= col_len or col >= row_len:
            return False

        if board[row][col] not in node.children:
            return False

        if (row, col) in visited:
            return False

        return True

    def dfs_util(
        self,
        row: int,
        col: int,
        board: List[List[str]],
        visited: Set[Tuple[int, int]],
        words_on_board: Set[str],
        node: TrieNode,
        word: str,
    ) -> bool:
        move_row = [1, 0, -1, 0]
        move_col = [0, 1, 0, -1]

        if not self.is_valid_cell(row, col, board, visited, node):
            return False

        visited.add((row, col))
        next_node = node.children[board[row][col]]
        word += board[row][col]

        if next_node.is_word:
            words_on_board.add(word)
            del node.children[board[row][col]]
            if len(node.children) == 1:
                child = node.children.values()[0]
                child.is_word = True

        for i in range(4):
            next_row = row + move_row[i]
            next_col = col + move_col[i]
            self.dfs_util(next_row, next_col, board, visited, words_on_board, next_node, word)

        visited.remove((row, col))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        words_on_board = set()
        visited = set()

        row_len = len(board[0])
        col_len = len(board)

        for row in range(col_len):
            for col in range(row_len):
                self.dfs_util(row, col, board, visited, words_on_board, root, '')

        return list(words_on_board)


m1 = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
w1 = ["oath", "pea", "eat", "rain"]

m2 = [
    ["a", "b"],
    ["c", "d"]
]
w2 = ["abcb"]

m3 = [["a", "a"]]
w3 = ["aa"]

m4 = [
    ["a", "b", "c"],
    ["a", "e", "d"],
    ["a", "f", "g"]
]
w4 = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]

m5 = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
w5 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

m6 = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
      ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
w6 = ["lllllll", "fffffff", "ssss", "s", "rr", "xxxx", "ttt", "eee", "ppppppp", "iiiiiiiii", "xxxxxxxxxx", "pppppp",
      "xxxxxx", "yy", "jj", "ccc", "zzz", "ffffffff", "r", "mmmmmmmmm", "tttttttt", "mm", "ttttt", "qqqqqqqqqq", "z",
      "aaaaaaaa", "nnnnnnnnn", "v", "g", "ddddddd", "eeeeeeeee", "aaaaaaa", "ee", "n", "kkkkkkkkk", "ff", "qq", "vvvvv",
      "kkkk", "e", "nnn", "ooo", "kkkkk", "o", "ooooooo", "jjj", "lll", "ssssssss", "mmmm", "qqqqq", "gggggg",
      "rrrrrrrrrr", "iiii", "bbbbbbbbb", "aaaaaa", "hhhh", "qqq", "zzzzzzzzz", "xxxxxxxxx", "ww", "iiiiiii", "pp",
      "vvvvvvvvvv", "eeeee", "nnnnnnn", "nnnnnn", "nn", "nnnnnnnn", "wwwwwwww", "vvvvvvvv", "fffffffff", "aaa", "p",
      "ddd", "ppppppppp", "fffff", "aaaaaaaaa", "oooooooo", "jjjj", "xxx", "zz", "hhhhh", "uuuuu", "f", "ddddddddd",
      "zzzzzz", "cccccc", "kkkkkk", "bbbbbbbb", "hhhhhhhhhh", "uuuuuuu", "cccccccccc", "jjjjj", "gg", "ppp",
      "ccccccccc", "rrrrrr", "c", "cccccccc", "yyyyy", "uuuu", "jjjjjjjj", "bb", "hhh", "l", "u", "yyyyyy", "vvv",
      "mmm", "ffffff", "eeeeeee", "qqqqqqq", "zzzzzzzzzz", "ggg", "zzzzzzz", "dddddddddd", "jjjjjjj", "bbbbb",
      "ttttttt", "dddddddd", "wwwwwww", "vvvvvv", "iii", "ttttttttt", "ggggggg", "xx", "oooooo", "cc", "rrrr", "qqqq",
      "sssssss", "oooo", "lllllllll", "ii", "tttttttttt", "uuuuuu", "kkkkkkkk", "wwwwwwwwww", "pppppppppp", "uuuuuuuu",
      "yyyyyyy", "cccc", "ggggg", "ddddd", "llllllllll", "tttt", "pppppppp", "rrrrrrr", "nnnn", "x", "yyy",
      "iiiiiiiiii", "iiiiii", "llll", "nnnnnnnnnn", "aaaaaaaaaa", "eeeeeeeeee", "m", "uuu", "rrrrrrrr", "h", "b",
      "vvvvvvv", "ll", "vv", "mmmmmmm", "zzzzz", "uu", "ccccccc", "xxxxxxx", "ss", "eeeeeeee", "llllllll", "eeee", "y",
      "ppppp", "qqqqqq", "mmmmmm", "gggg", "yyyyyyyyy", "jjjjjj", "rrrrr", "a", "bbbb", "ssssss", "sss", "ooooo",
      "ffffffffff", "kkk", "xxxxxxxx", "wwwwwwwww", "w", "iiiiiiii", "ffff", "dddddd", "bbbbbb", "uuuuuuuuu", "kkkkkkk",
      "gggggggggg", "qqqqqqqq", "vvvvvvvvv", "bbbbbbbbbb", "nnnnn", "tt", "wwww", "iiiii", "hhhhhhh", "zzzzzzzz",
      "ssssssssss", "j", "fff", "bbbbbbb", "aaaa", "mmmmmmmmmm", "jjjjjjjjjj", "sssss", "yyyyyyyy", "hh", "q",
      "rrrrrrrrr", "mmmmmmmm", "wwwww", "www", "rrr", "lllll", "uuuuuuuuuu", "oo", "jjjjjjjjj", "dddd", "pppp",
      "hhhhhhhhh", "kk", "gggggggg", "xxxxx", "vvvv", "d", "qqqqqqqqq", "dd", "ggggggggg", "t", "yyyy", "bbb",
      "yyyyyyyyyy", "tttttt", "ccccc", "aa", "eeeeee", "llllll", "kkkkkkkkkk", "sssssssss", "i", "hhhhhh", "oooooooooo",
      "wwwwww", "ooooooooo", "zzzz", "k", "hhhhhhhh", "aaaaa", "mmmmm"]

m7 = [
    ["o", "a", "b", "n"],
    ["o", "t", "a", "e"],
    ["a", "h", "k", "r"],
    ["a", "f", "l", "v"]
]
w7 = ["oa", "oaa"]


if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    # print(sol.findWords(m1, w1))
    # print(sol.findWords(m2, w2))
    # print(sol.findWords(m3, w3))
    # print(sol.findWords(m4, w4))
    # print(sol.findWords(m5, w5))
    # print(sol.findWords(m6, w6))
    print(sol.findWords(m7, w7))
    print("----%s seconds----" % (time.time() - start_time))
