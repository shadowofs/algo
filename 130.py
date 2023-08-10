from typing import List

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        accessed = set()
        rows = len(board)
        cols = len(board[0])

        def mark(r, c):
            if (r, c) in accessed or r < 0 or c < 0 or r >= rows or c >= cols:
                return

            accessed.add((r, c))
            if board[r][c] == 'X':
                return

            for direction in directions:
                mark(r + direction[0], c+ direction[1])

        for j in range(1, cols-1):
            mark(0, j)
            mark(rows-1, j)

        for i in range(1, rows-1):
            mark(i, 0)
            mark(i, cols-1)

        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if (i,j) not in accessed:
                    board[i][j] = 'X'

        return


if __name__ == '__main__':
    x = [["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]
    print("input:")
    for row in x:
        print(row)

    Solution().solve(x)
    print("output:")
    for row in x:
        print(row)