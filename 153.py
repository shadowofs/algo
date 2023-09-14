from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            elif l + 1 == r:
                return nums[r]

            mid = (l + r) // 2

            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid


        return nums[l]


if __name__ == "__main__":
    print(Solution().findMin([3,4,5,1,2]))