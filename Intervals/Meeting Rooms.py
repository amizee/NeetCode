from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda interval: interval.start)
        prevEnd = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if prevEnd > interval.start:
                return False
            prevEnd = max(prevEnd, interval.end)
        return True