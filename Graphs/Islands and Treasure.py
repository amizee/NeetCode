from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647 
        R, C = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit = set()
        queue = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        
        dist = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr == R or c + dc == C or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] < 0):
                        continue
        
                    grid[r + dr][c + dc] = dist
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            dist += 1
            
# Intuition: multi-source BFS. Instead of checking the shortest path from each land cell to the nearest treasure, start from each chest and move outwards using BFS.
# BFS ensures that as you move outward, this must be the minimum distance from any land cells to the nearest treasure.
# i.e. you add cells by level to the queue. After each iteration, every land cell in the queue is equidistant to a nearby treasure.


