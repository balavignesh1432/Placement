def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    # TC: O(M*N), SC: O(1), M*N for storing result
    res = []
    # Initialize window Size
    lowRow = lowCol = 0
    highRow = len(matrix) - 1
    highCol = len(matrix[0]) - 1
    # Do until valid Window Size
    while lowRow <= highRow and lowCol <= highCol:
        # Right Direction: Start from lowCol
        for col in range(lowCol, highCol + 1):
            res.append(matrix[lowRow][col])
        # Bottom Direction: Start From lowRow + 1, as lowRow already included in previous loop
        for row in range(lowRow + 1, highRow + 1):
            res.append(matrix[row][highCol])
        # If both are same, then already included from 1st loop
        if lowRow != highRow:
            # Start From highCol - 1, as highCol already included in previous loop
            for col in range(highCol - 1, lowCol - 1, -1):
                res.append(matrix[highRow][col])
        # If both are same, then already included from 2nd loop
        if lowCol != highCol:
            # Start From highCol - 1, as highCol already included in previous loop
            # Do not include lowRow, as it is already included in first loop
            for row in range(highRow - 1, lowRow, -1):
                res.append(matrix[row][lowCol])
        # Update window size
        lowRow += 1
        lowCol += 1
        highRow -= 1
        highCol -= 1
    return res