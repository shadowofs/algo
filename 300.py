from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        cache[0] = 1
        res = 0

        def dp(i: int) -> int:
            if cache[i]:
                return cache[i]

            n = 1
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue

                dpj = dp(j)
                if dpj + 1 > n:
                    n = dpj + 1

            cache[i] = n
            return n

        for i in range(len(nums)):
            dpi = dp(i)
            if res < dpi:
               res = dpi

        return res


if __name__ == "__main__":
    print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))