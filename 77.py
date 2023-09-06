from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return [list(i) for i in combinations(iterable=range(1, n + 1), r=k)]

if __name__ == "__main__":
    print(Solution().combine(4, 2))