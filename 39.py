from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        val = 0
        candidates.sort()

        def step():
            nonlocal val
            nonlocal cur
            nonlocal res
            for v in candidates:
                if v + val > target:
                    return

                if len(cur) > 0 and cur[-1] > v:
                    continue

                cur.append(v)
                val += v

                if val == target:
                    res.append(cur[:])
                else:
                    step()

                cur.pop(-1)
                val -= v

        step()
        return res


if __name__ == "__main__":
    print(Solution().combinationSum([2,3,5], 8))