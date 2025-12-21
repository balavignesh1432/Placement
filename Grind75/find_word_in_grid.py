def searchWord(self, grid, word):
    # Find the word in 8 directions
    # At each step only go in already chosen in direction
    # Zig zag not possible, so pass chosen direction as parameter
    # Base At last letter, return equality of the letters
    # Call for 8 directions starting from each position, if any one returns True
    # Add to list and break.
    # TC: O(M * N * K * 8), SC: O(K)
    # Can be replaced with iteration to save space since only one direction
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    def helper(row, col, d, index):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or word[index] != grid[row][col]:
            return False
        if index == len(word) - 1:
            return word[index] == grid[row][col]
        rd, cd = directions[d]
        return helper(row + rd, col + cd, d, index + 1)
    
    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(len(directions)):
                if helper(i, j, d, 0):
                    res.append([i, j])
                    break
    return res