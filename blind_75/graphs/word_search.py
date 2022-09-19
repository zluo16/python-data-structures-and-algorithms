import collections
import time
from typing import List


class Solution:

    def __init__(self):
        self.x_vex = [1, 0, -1, 0]
        self.y_vex = [0, 1, 0, -1]

    def is_valid_cell(self, row: int, col: int, visited: List[List[bool]]) -> bool:
        if row < 0 or col < 0 or row >= len(visited) or col >= len(visited[0]):
            return False

        if visited[row][col]:
            return False

        return True

    def dfs_for_word(self, row: int, col: int, visited: List[List[bool]], board: List[List[str]], word_q) -> bool:
        if len(word_q) == 0:
            return True

        if not self.is_valid_cell(row, col, visited):
            return False

        if board[row][col] == word_q[0]:
            visited[row][col] = True
            word_q.popleft()

            for i in range(4):
                next_row = row + self.y_vex[i]
                next_col = col + self.x_vex[i]
                self.dfs_for_word(next_row, next_col, visited, board, word_q)

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    visited_mat = [
                        [False for i in range(len(board[0]))]
                        for j in range(len(board))
                    ]
                    word_q = collections.deque([*word])
                    self.dfs_for_word(row, col, visited_mat, board, word_q)
                    if len(word_q) == 0:
                        return True

        return False


b1 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

b2 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

b3 = [
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]
]

b4 = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

b5 = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"]
]

b6 = [
    ["a", "b"],
    ["c", "d"]
]

if __name__ == '__main__':
    sol = Solution()

    start_time = time.time()
    print(sol.exist(b1, "ABCCED"))
    print(sol.exist(b2, "SEE"))
    print(sol.exist(b3, "AAB"))
    print(sol.exist(b4, "ABCB"))
    print(sol.exist(b5, "ABCESEEEFS"))
    print(sol.exist(b6, "abcd"))
    print("----%s seconds----" % (time.time() - start_time))
