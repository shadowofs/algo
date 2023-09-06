from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = [(startGene, 0)]
        visited = [False] * len(bank)

        def diff(g1, g2: str) -> int:
            count = 0
            for i in range(8):
                if g1[i] != g2[i]:
                    count += 1

            return count

        while queue:
            cur = queue.pop(0)
            for idx, step in enumerate(bank):
                if visited[idx]:
                    continue

                d = diff(step, cur[0])
                if d > 1:
                    continue

                if step == endGene:
                    return cur[1] + 1

                visited[idx] = True
                queue.append((step, cur[1] + 1))

        return -1