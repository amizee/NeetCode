class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, height, visit):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or (r, c) in visit):
                return

            if heights[r][c] >= height:
                visit.add((r, c))
                dfs(r + 1, c, heights[r][c], visit)
                dfs(r - 1, c, heights[r][c], visit)
                dfs(r, c + 1, heights[r][c], visit)
                dfs(r, c - 1, heights[r][c], visit)
            
        # Pacific
        for i in range(COLS):
            dfs(0, i, heights[0][i], pacific)
        for i in range(ROWS):
            dfs(i, 0, heights[i][0], pacific)
        
        # Atlantic
        for i in range(COLS):
            dfs(ROWS - 1, i, heights[ROWS - 1][i], atlantic)
        for i in range(ROWS):
            dfs(i, COLS - 1, heights[i][COLS - 1], atlantic)
        
        res = []
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])
        return res

# Intuition: instead of running a brute force BFS from each cell and checking if it reaches both oceans
# start from all cells adjacent to each ocean and DFS to cells with higher heights, which means that this cell can reach that ocean.
# Use a set to store all valid cells for each ocean so each cell is visited only once.
# Now that we have all cells that can reach both oceans, just check if they're in both sets and add it to res.