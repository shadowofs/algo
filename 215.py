import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])

        return heap[0]


if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))