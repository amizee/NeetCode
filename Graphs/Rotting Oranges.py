from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))

        count = 0
        while queue:
            adjExists = False
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS
                        or grid[r + dr][c + dc] == 0 or (r + dr, c + dc) in visit):
                        continue

                    grid[r + dr][c + dc] = 2
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                    adjExists = True
                    
            if adjExists:
                count += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return count
        
# Intuition: multi-source BFS again similar to Islands and Treasure. The only difference is that as you perform BFS each fresh fruit is marked as rotten to prevent repeated work and only newly rotten fruits can be added to the queue as it can't spread through empty cells.
# To ensure count is correct, I checked that there was at least one fresh fruit adjacent to a rotten fruit in each iteration, otherwise it's an impossible state or all fruits have been turned rotten already.
# To make the code slightly more efficient, in the initial check for rotten fruits you can count the number of fresh fruits and decrement it and check this value to see if it's complete.