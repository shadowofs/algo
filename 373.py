from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        added = set()
        for _ in range(k):
            if not h:
                break

            cur = heappop(h)
            i, j = cur[1], cur[2]
            if (i, j+1) not in added and j + 1 < len(nums2):
                added.add((i, j+1))
                heappush(h, (nums1[i] + nums2[j+1], i, j+1))

            if (i+1, j) not in added and i + 1 < len(nums1):
                added.add((i+1, j))
                heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))

            res.append([nums1[i], nums2[j]])

        return res


if __name__ == "__main__":
    print(Solution().kSmallestPairs([1,1,2], [1,2,3], 10))