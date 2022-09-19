import collections
from typing import List


def dfs_on_matrix(matrix: List[List[int]]) -> List[int]:

    x_vex = [0, 1, 0, -1]
    y_vex = [-1, 0, 1, 0]

    visited = [
        [False for i in range(len(matrix[0]))]
        for j in range(len(matrix))
    ]

    matrix_nodes = []

    def dfs_util(row: int, col: int, m: List[List[int]]):
        st = collections.deque()
        st.append([row, col])

        while len(st) > 0:
            curr = st.pop()
            r = curr[0]
            c = curr[1]

            if r < 0 or c < 0 or r >= len(m[0]) or c >= len(m):
                continue

            if visited[r][c]:
                continue

            visited[r][c] = True

            matrix_nodes.append(m[r][c])

            for i in range(4):
                adj_x = r + x_vex[i]
                adj_y = c + y_vex[i]
                st.append([adj_x, adj_y])

    dfs_util(0, 0, matrix)

    return matrix_nodes


grid = [
    [-1, 2, 3],
    [0, 9, 8],
    [1, 0, 1],
]

print(dfs_on_matrix(grid))
