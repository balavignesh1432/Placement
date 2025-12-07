def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Using HashSet to track seen numbers in rows, columns and boxes
    # Value must be a digit between 1-9, '.' indicates empty cell
    # For each cell, check if the number is already seen in the corresponding row, column or box
    # For boxes, use (row // 3, col // 3) to identify the box index
    # If any number is repeated in any row, column or box, return False
    # Time: O(9*9) = O(1), Space: O(9*9) = O(1)
    row = defaultdict(set)
    col = defaultdict(set)
    box = defaultdict(set)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].isdigit():
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                if board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])
                cell = (i // 3, j // 3)                
                if board[i][j] in box[cell]:
                    return False
                box[cell].add(board[i][j])
    return True
            