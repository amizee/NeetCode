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


    