class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or grid[r][c] == 0 or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            return (1 + dfs(r, c + 1) + dfs(r, c - 1)
                + dfs(r + 1, c) + dfs(r - 1, c))
    
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(dfs(r, c), maxArea)
        
        return maxArea

# Intuition: loop through all cells to find all possible islands. When you find a land cell (1), run DFS to find all cells that belong to this island. 
# Use 1 + dfs() so that each cell contribues 1 to the area if valid and return 0 if the cell is invalid.