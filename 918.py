from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        total = sum(nums)
        globalmax = -30001
        leftmin = 30001
        leftmax = -30001
        leftsum = 0
        for i in range(len(nums)):
            leftsum += nums[i]
            globalmax = max(leftsum, leftsum - leftmin, globalmax)
            if i != len(nums) - 1:
                globalmax = max(total - leftsum, total - leftsum + leftmax, globalmax)
            leftmin = min(leftmin, leftsum)
            leftmax = max(leftmax, leftsum)

        return globalmax

if __name__ == "__main__":
    print(Solution().maxSubarraySumCircular([-3,-2,-3]))