from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        row = [1, 1]
        counter = rowIndex - 2

        while counter > -1:
            last_idx = len(row) - 1
            new_row = [1] + [0] * last_idx + [1]
            for i in range(1, len(new_row) - 1):
                new_val = row[i - 1] + row[i]
                new_row[i] = new_val
            row = new_row
            counter -= 1

        return row
