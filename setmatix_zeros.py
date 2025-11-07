def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # Use separate memory for storing positions in 1st run. (Can use set also)
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0        
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] == 0 or cols[j] == 0:   #Check if the row, or col needs to be zero
                    matrix[i][j] = 0

        # TC - O(M*N), SC - O(M + N)
        
        # Optimal SC, Intuition using 1st row/col itself as a marker
        # To store marker if first col needs to be zeroed
        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j == 0:  # If first col needs to be zeroed, then mark
                        col0 = 0
                    else:   # Otherwise mark in the 1st row, for other columns except 1st col
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # Iterate except first row and col
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # Check if that row or col needs to be zeroed using 1st row, col
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Now check if first row needs to be zeroed
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # Check if first col needs to be zeroed
        if col0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
    
    # TC - O (M*N), SC - O(1)