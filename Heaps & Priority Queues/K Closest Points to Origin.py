class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p[0], p[1]
            distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(heap, (-distance, p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
  
# Intuition: create a max heap by multiplying the distance by -1, because heaps, tuples and lists are sorted by the first value.
# For heap problems, try to only keep the minimum amount of elements needed, i.e. "k" in this case.