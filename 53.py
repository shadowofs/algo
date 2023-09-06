from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        leftMin = min(nums[0], 0)
        res = nums[0]

        for cur in range(1, len(nums)):
            nums[cur] += nums[cur-1]
            if nums[cur] - leftMin > res:
                res = nums[cur] - leftMin

            if nums[cur] < leftMin:
                leftMin = nums[cur]

        return res

if __name__ == "__main__":
    print(Solution().maxSubArray([-2, -1]))