from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = set()
        for i in range(k):
            if nums[i] not in counter:
                counter.add(nums[i])
            else:
                return True

        for i in range(k, len(nums)):
            if nums[i] in counter:
                return True

            counter.add(nums[i])
            counter.remove(nums[i - k])

        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1,2,3,1], 3))