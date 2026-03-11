from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        n = len(intervals)
        s, e = intervals[0]
        
        for i in range(1, n):
            newInterval = intervals[i]
            if newInterval[0] <= e:
                e = max(newInterval[1], e)
            else:
                res.append([s, e])
                s, e = newInterval
        res.append([s, e])
        return res

# Intuition: if there's an overlap, update the end value of to "merge" the intervals
# If there's no overlap, add the previous interval. So at the end, we need to add the last interval and potentitally it's a merged interval so it doesn't reach the first res.append().