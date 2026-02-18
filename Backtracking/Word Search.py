from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()

        def backtrack(i, r, c):
            if i == len(word):
                return True
            
            if min(r, c) < 0 or r >= R or c >= C or board[r][c] != word[i] or (r, c) in visited:
                return False
        
            visited.add((r, c))

            down = backtrack(i + 1, r + 1, c)
            up = backtrack(i + 1, r - 1, c) 
            right = backtrack(i + 1, r, c + 1) 
            left = backtrack(i + 1, r, c - 1)

            visited.remove((r, c))
            if left or right or up or down:
                return True
            return False
    
        for r in range(R):
            for c in range(C):
                if backtrack(0, r, c):
                    return True
        return False
    
# Intuition: matrix DFS! by trying to start the word from each cell and exploring up, left, down or right.
# Use a hashset to see if a cell on the current path has already been explored.
# Check out of bounds, if the current character matches the word or if this cell has been explored.