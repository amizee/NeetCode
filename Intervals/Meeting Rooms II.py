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
    
# Intuition: sort the start and end times into two separate arrays. The number of rooms needed is the highest number of meetings occurring at a single point in time.
# So for each end time, calculate all the meetings that start before it.
# If the next meeting starts BEFORE the current one ends, then they will happen at the same time so increment s and activeMeetings
# If the next meeting starts AFTER the current one ends, then they won't happen at the same time so increment e and decrement activeMeetings

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
            
        return len(minHeap)

# Intuition: basically if a meeting starts before the earliest meeting has ended (so no existing rooms are free), add a room and push the end time onto the heap.

# Note: don't get stuck into following methods of other interval questions, may use other data structures and old techniques
# Intervals is really about finding an idea that works rather than the code being challenging, draw pictures to help.



        