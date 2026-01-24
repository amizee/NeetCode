class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        for row in range(9):
            for i in range(9):
                if board[row][i] in rowSet:
                    return False
                if board[row][i] != ".":
                    rowSet.add(board[row][i])
            rowSet = set()
        
        colSet = set()
        for col in range(9):
            for i in range(9):
                if board[i][col] in colSet:
                    return False
                if board[i][col] != ".":
                    colSet.add(board[i][col])
            colSet = set()
        
        squares = {}
        for i in range(9):
            squares[i] = set()
        
        for i in range(9):
            for j in range(9):
                row = i // 3
                col = math.ceil(j // 3)
                sqr = (row * 3) + col
                if board[i][j] in squares[sqr]:
                    return False
                if board[i][j] != ".":
                    squares[sqr].add(board[i][j])

        return True

# Intuition: Smart way of looping through rows and  columns, and calculating which square a sub-box belongs to based on its row and column.