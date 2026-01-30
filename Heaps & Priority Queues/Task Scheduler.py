import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = {}
        for t in tasks:
            taskCount[t] = taskCount.get(t, 0) + 1
        
        maxHeap = []
        for count in taskCount.values():
            heapq.heappush(maxHeap, -count)

        queue = deque() # [-count, idleTime]
        time = 0
        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]
            else:
                count = heapq.heappop(maxHeap) + 1
                if count < 0:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                count = queue.popleft()[0]
                heapq.heappush(maxHeap, count)
        return time

# Intuition: use a heap to keep track of the most frequent task which has the highest priority. Use a queue to maintain the order of tasks and implement the cooldown period.
# Every time you pop from the heap, this "completes" the task so you reduce the frequency then add it to the queue to "cooldown" if it's not fully complete
# If there's nothing in the heap, then all the tasks are on cooldown and the CPU must idle until the earliest task goes off cooldown
# In each iteration, check if there's a task thats no longer on cooldown