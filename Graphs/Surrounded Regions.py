class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or (r, c) in visit or board[r][c] == "X"): 
                return 
            
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS - 1, i)
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit:
                    board[r][c] = "X"
        

# Intuition: again the opposite case works, instead of starting from the surrounded regions in the middle start from 'O's on the border.
# DFS through all 'O' regions connected to the border and add it to a set, meaning that any remaining O's must be surrounded.
# Alternatively you could mark all border connected regions in place with a temporary mark 'T', and then in the final loop change it back to 'O'.
# Time and space complexity: O(m * n)