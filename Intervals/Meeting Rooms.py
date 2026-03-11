from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

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

# Intuition: check for overlap of any meetings (i.e. if any meeting starts before one has ended)