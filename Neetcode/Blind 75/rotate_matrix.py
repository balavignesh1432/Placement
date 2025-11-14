def rotate(self, matrix: List[List[int]]) -> None:
    
    # Using Four Pointers on the corners of window, rotate corner values but storing one corner
    # Then move the four pointers clockwise for every window size
    # Update the window size [Outer box to innner Box]
    # Until valid window size, perform this
    low = 0
    high = len(matrix) - 1
    while low < high:
        for i in range(high - low):
            store = matrix[low][low + i]
            matrix[low][low + i] = matrix[high - i][low]
            matrix[high - i][low] = matrix[high][high - i]
            matrix[high][high - i] = matrix[low + i][high]
            matrix[low + i][high] = store
        low += 1
        high -= 1 
    
    # Matrix Operations - Intuition: 90 Degree clockwise can be achieved using transposing last row as first column
    # But since transposing last row as first column can not be done in place, 
    # But Transposing first row and first col can be done in place
    # So reverse the order of rows, and then transpose in place
    # TC: O(N*2), SC: O(!)
    matrix.reverse()
    # Transposing matrix, row <-> Swap
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):  # Transpose moves from outer ring to inner, So col same as row initially
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
