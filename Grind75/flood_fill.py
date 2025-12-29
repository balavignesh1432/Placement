def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    # DFS approach
    # Visited set not needed as color change marks visited
    # Base Case: If out of bounds or color is not the same as original, then return
    # Modify the color and mark as visited
    # Explore in all 4 directions
    # Time: O(M * N) where M is number of rows and N is number of columns
    # Space: O(M * N) for the recursion stack
    source = image[sr][sc]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if source == color:
        return image
    def helper(row, col):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] != source:
            return
        image[row][col] = color
        for rd, cd in directions:
            helper(row + rd, col + cd)
    helper(sr, sc)
    return image

    

    # BFS approach
    # Visited set not needed as color change marks visited
    # Base Case: If out of bounds or color is not the same as original, then continue
    # Time: O(M * N) where M is number of rows and N is number of columns
    # Space: O(M * N) for the queue
    source = image[sr][sc]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    if source == color:
        return image
    q = deque()
    q.append([sr, sc])
    while q:
        row, col = q.popleft()
        image[row][col] = color
        for rd, cd in directions:
            r = row + rd
            c = col + cd
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != source:
                continue
            q.append([r, c])
    return image