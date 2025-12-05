# N-Queens Problem
# Check Condition: No two queens threaten each other
# Use column and diagonal sets to track threats
# IMP: No need of row set, as column set is sufficient as only one queen per row
# IMP: To identify diagonals:
# Main diagonal: row + col is constant for a given diagonal
# Secondary diagonal: row - col is constant for a given diagonal
# Initialize board with '.' and place 'Q' for queens at each valid position
# Backtrack when a position leads to no solution, removing queens and updating sets accordingly
# Base Case: When all queens are placed (i == n), add the current board configuration to results
# Time: O(N!) in the worst case, as we try to place queens row by row
# Space: O(N) for the board and sets used to track columns and diagonals
def solveNQueens(self, n: int) -> List[List[str]]:
    nQueens = []
    board = [["."] * n for _ in range(n)]
    col = set()
    mainD = set()
    secD = set()
    def helper(i, pos):
        if i == n:
            nQueens.append(pos.copy())
            return
        
        for j in range(n):
            if j in col or (i + j) in mainD or (i - j) in secD:
                continue
            board[i][j] = 'Q'
            col.add(j)
            mainD.add(i + j)
            secD.add(i - j)
            pos.append("".join(board[i]))
            
            helper(i + 1, pos)
            
            col.remove(j)
            mainD.remove(i + j)
            secD.remove(i - j)
            pos.pop()
            board[i][j] = "."

    helper(0, [])
    return nQueens