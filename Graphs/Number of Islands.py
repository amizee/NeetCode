from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, visited):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or grid[r][c] == "0" or (r, c) in visited):
                return False 
       
            visited.add((r, c))

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, visited):
                    res += 1
        
        return res

# Intuition: an island can start from any cell so loop through every cell in the matrix.
# If you find a cell that's land (i.e. 1), check all 4 directions to find all the cells that are part of that island. Add it to the visited set to avoid duplicates and infinite paths.
# Once we finish checking all directions, that makes one island so we add 1 to res.
