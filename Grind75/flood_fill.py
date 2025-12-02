def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    # DFS approach
    # Base Case: If already visited or out of bounds or color is not the same as original, then return
    # Modify the color and mark as visited
    # Explore in all 4 directions
    # Time: O(M * N) where M is number of rows and N is number of columns
    # Space: O(M * N) for the recursion stack and visited set
    change = image[sr][sc]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = set()
    def helper(row, col):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or (row, col) in visited or image[row][col] != change:
            return
        image[row][col] = color
        visited.add((row, col))
        for rd, cd in directions:
            helper(row + rd, col + cd)
    helper(sr, sc)
    return image
    

    # BFS approach
    # Base Case: If already visited or out of bounds or color is not the same as original, then continue
    # Time: O(M * N) where M is number of rows and N is number of columns
    # Space: O(M * N) for the queue and visited set
    q = deque()
    q.append([sr, sc])
    while q:
        row, col = q.popleft()
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or (row, col) in visited or image[row][col] != change:
            continue
        image[row][col] = color
        visited.add((row, col))
        for rd, cd in directions:
            q.append([row + rd, col + cd])
    return image