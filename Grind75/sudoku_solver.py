def solveSudoku(self, board: List[List[str]]) -> None:
    # Using Backtracking to fill the Sudoku board
    # Track used numbers in rows, columns and boxes using hash sets
    # Initially fill the hash sets with existing numbers
    # Identify empty spaces to fill, add to spaces list
    # For each empty space, try numbers 1-9
    # If valid (not in row, col, box), place number and recurse to next empty space
    # If placing number leads to solution, return True
    # If not, backtrack by removing number and trying next number
    # Time: O(9^(m*n)) in worst case, Space: O(m*n) for recursion stack and hash sets
    row = defaultdict(set)
    col = defaultdict(set)
    box = defaultdict(set)
    spaces = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].isdigit():
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3, j//3)].add(board[i][j])
            else:
                spaces.append([i, j])

    def helper(index):
        if index == len(spaces):                # All spaces filled
            return True
        i, j = spaces[index]                    # Get indices of the empty space
        for num in map(str, range(1, 10)):      # Since board contains strings
            if num in row[i] or num in col[j] or num in box[(i//3, j//3)]:  # If num already used
                continue
            row[i].add(num)
            col[j].add(num)
            box[(i//3, j//3)].add(num)
            board[i][j] = num
            if helper(index + 1):               # If placing num leads to solution
                return True                     # Return True up the recursion stack
            row[i].remove(num)                  # Backtrack: remove num from row, col, box
            col[j].remove(num)
            box[(i//3, j//3)].remove(num)
            board[i][j] = "."
        return False
    helper(0)