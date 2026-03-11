from typing import List
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()

        s, e = 0, 0
        activeMeetings, minRooms = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                activeMeetings += 1
                s += 1
            else:
                activeMeetings -= 1
                e += 1
            minRooms = max(minRooms, activeMeetings)
            
        return minRooms

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
            
        return len(minHeap)
        



        