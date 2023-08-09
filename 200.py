# https://leetcode.cn/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150
from typing import List

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        accessed = []
        count = 0
        for i in range(rows):
            accessed.append([False] * cols)

        def traverse(pos: (int, int)):
            nonlocal grid
            for offset in offsets:
                ni, nj = pos[0] + offset[0], pos[1] + offset[1]

                if ni < 0 or ni >= rows:
                    continue

                if nj < 0 or nj >= cols:
                    continue

                if accessed[ni][nj]:
                    continue

                accessed[ni][nj] = True
                if grid[ni][nj] == '0':
                    continue

                traverse((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if accessed[i][j]:
                    continue

                accessed[i][j] = True
                if grid[i][j] == '0':
                    continue

                count += 1
                traverse((i, j))

        return count

if __name__ == '__main__':
    print(Solution().numIslands(grid = [["0","1","0"],["1","0","1"],["0","1","0"]]))

