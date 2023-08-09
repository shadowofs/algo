from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        left, right = 0, len(intervals)
        if intervals[0][0] >= newInterval[0]:
            right = 0
            left = -1

        while left + 1 < right:
            mid = int((left + right) / 2)
            if intervals[mid][0] >= newInterval[0]:
                right = mid
            else:
                left = mid

        if left >= 0 and intervals[left][1] >= newInterval[0]:
            intervals[left][1] = max(newInterval[1], intervals[left][1])
            right = left
        else:
            intervals.insert(right, newInterval)

        if len(intervals) > 1:
            while right + 1 < len(intervals) and intervals[right][1] >= intervals[right + 1][0]:
                intervals[right][1] = max(intervals[right + 1][1], intervals[right][1])
                intervals.pop(right+1)

        return intervals


if __name__ == '__main__':
    print(Solution().insert([[0,1],[5,5],[6,7],[9,11]], [12,21]))