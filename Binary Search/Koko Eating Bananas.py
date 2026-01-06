class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = 0
        for p in piles:
            maxK = max(p, maxK)

        low, high = 1, maxK
        minK = float("inf")
        while low <= high:
            hours = h
            k = (low + high) // 2
            for i in range(len(piles)):
                hours -= math.ceil(piles[i] / k)

            if hours >= 0:
                minK = min(k, minK)
                high = k - 1
            else:
                low = k + 1
            
        return minK
    
# Intuition: max k equals the number of bananas in a pile, perform binary search on k and check if k is fast enough
# If not, check the "right" of k and vice versa