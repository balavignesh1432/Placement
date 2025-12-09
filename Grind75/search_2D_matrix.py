def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # Binary Search approach
    # First, perform binary search on the last elements of each row to find the potential row
    # Then, perform binary search on that row to find the target
    # For row search, if target is less than mid, move right to mid, because mid could be the row
    # For column search, standard binary search, move mid - 1 or mid + 1 accordingly
    # Time: O(log M + log N) = log(M * N) where M is number of rows and N is number of columns
    # Space: O(1)
    left = 0
    right = len(matrix) - 1
    while left < right:
        mid = (left + right) // 2
        if target > matrix[mid][-1]:
            left = mid + 1
        elif target < matrix[mid][-1]:
            right = mid
        else:
            return True
    
    row = right # Or Left, since left == right

    left = 0
    right = len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return True
    return False

    # Binary search on whole matrix considered 1D sorted array
    # Divide by number of cols to get row, and remainder is col
    # Left at 0, right at last cell, Find middle, get the indices
    # TC: O(Log M*N), SC: O(1)
    left = 0
    right = (len(matrix) * len(matrix[0])) - 1
    while left <= right:
        mid = (left + right) // 2
        i, j = mid // len(matrix[0]), mid % len(matrix[0])
        if target > matrix[i][j]:
            left = mid + 1
        elif target < matrix[i][j]:
            right = mid - 1
        else:
            return True
    return False