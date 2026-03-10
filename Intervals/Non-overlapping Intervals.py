from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        n = len(intervals)
        prevEnd = intervals[0][1]

        for i in range(1, n):
            newInterval = intervals[i]
            if prevEnd > newInterval[0]:
                res += 1
                prevEnd = min(prevEnd, newInterval[1])
            else:
                prevEnd = newInterval[1]
        return res