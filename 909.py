from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        size = length * length
        accessed = [False] * size

        def getBoard(idx: int) -> int:
            div = int(idx / length)
            row = length - div - 1

            col = idx % length
            if div % 2 == 1:
                col = length - 1 - col

            return board[row][col]

        queue = [(0, 0)]
        while queue:
            cur = queue.pop(0)
            step = -1

            for j in range(cur[0] + 1, min(cur[0] + 7, size)):
                nxt = getBoard(j)
                if nxt == -1:
                    step = j
                elif not accessed[nxt - 1]:
                    accessed[nxt - 1] = True
                    if nxt == size:
                        return cur[1] + 1
                    queue.append((nxt-1, cur[1] + 1))

            if step != -1 and not accessed[step]:
                accessed[step] = True
                if step == size - 1:
                    return cur[1] + 1
                queue.append((step, cur[1] + 1))

        return -1


if __name__ == "__main__":
    board = [[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]
    for row in board:
        print(row)
    print(Solution().snakesAndLadders(board))