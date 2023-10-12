from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]

        dp = {size - 1: nums[-1]}

        def dprob(i: int) -> int:
            if i >= size:
                return 0

            if i in dp:
                return dp[i]

            dp[i] = max(nums[i] + dprob(i + 2), nums[i + 1] + dprob(i + 3))
            return dp[i]

        return dprob(0)


def max(a, b: int):
    if a > b:
        return a
    return b


if __name__ == "__main__":
    print(Solution().rob([1,2,3,1]))