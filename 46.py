from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        selected = []
        selectedIdx = [False] * len(nums)
        size = len(nums)
        res = []

        def select():
            for i, num in enumerate(nums):
                if selectedIdx[i]:
                    continue

                selectedIdx[i] = True
                selected.append(num)
                if len(selected) == size:
                    res.append(selected[:])
                else:
                    select()
                selectedIdx[i] = False
                selected.pop(-1)

        select()
        return res

if __name__ == "__main__":
    print(Solution().permute([1,2,3]))