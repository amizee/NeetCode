from typing import List

# Sliding window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit

# One pass, keeping track of the minimum price so far (highest potential profit)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] > minPrice:
                maxProfit = max(maxProfit, prices[i] - minPrice)
            else:
                minPrice = prices[i]
        return maxProfit
            

        