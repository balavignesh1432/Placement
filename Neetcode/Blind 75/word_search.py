def exist(self, board: List[List[str]], word: str) -> bool:
    # Backtracking: For every cell start dfs
    # In each step, add cell to path set, explore all 4 directions, remove cell from path set.
    # Apart from row, col use index to keep checking word[index] is equal to the grid character.
    # Base Case: When out of bounds, or already in path or character not equal to word's index return False
    # If index reached end of word, then word is present, so return True
    # TC: O(C * 4^N), where C is no.of. cells, N is word length, SC: O(N)
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    path = set()
    def dfs(row, col, index):
        if index == len(word):  # If end of word reached, then return True
            return True
        # Check for bounds, in path and equality for the word's character
        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1 or (row, col) in path or board[row][col] != word[index]:
            return False
        path.add((row, col))    # Add to set
        for rd, cd in directions:   # Explore directions
            if dfs(row + rd, col + cd, index + 1):  # If any direction results in true,return True
                return True 
        path.remove((row, col)) # Remove from set, this ensures it is part of some other dfs path
        return False    # If could not proceed anywhere return False
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                    return True
    return False