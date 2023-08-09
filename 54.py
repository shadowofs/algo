from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        i, j = 0, 0
        l, r, u, d = -1, len(matrix[0]), 0, len(matrix)
        total = len(matrix) * len(matrix[0])
        direction = 0
        ans = [0] * total
        cur = 1
        ans[0] = matrix[0][0]
        while cur < total:
            if direction == 0:
                if j + 1 < r:
                    j += 1
                    ans[cur] = matrix[i][j]
                    cur += 1
                else:
                    direction = 1
                    r = j
            elif direction == 1:
                if i + 1 < d:
                    i += 1
                    ans[cur] = matrix[i][j]
                    cur += 1
                else:
                    d = i
                    direction = 2
            elif direction == 2:
                if j - 1 > l:
                    j -= 1
                    ans[cur] = matrix[i][j]
                    cur += 1
                else:
                    l = j
                    direction = 3
            elif direction == 3:
                if i - 1 > u:
                    i -= 1
                    ans[cur] = matrix[i][j]
                    cur += 1
                else:
                    direction = 0
                    u = i
        return ans