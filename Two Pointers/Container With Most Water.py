class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            minHeight = min(heights[l], heights[r])
            area = minHeight * (r - l)
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

# Intuition: start at the edges to get the highest area potential, and always move the smaller height pointer inwards.