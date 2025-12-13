def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    visited = set()
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    maxArea = 0
    # To handle island size, For every bfs call, initialize counter to 0
    # For every non visited valid land, add to counter
    # Return the counter
    # # Mark visited to avoid revisiting.
    # TC: O(M * N), SC: O(M * N)
    # Every cell is visited at most once
    def bfs(row, col):
        q = deque()
        q.append([row, col])
        island = 0
        while q:
            row, col = q.popleft()
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 0:
                continue
            visited.add((row, col))
            island += 1
            for rd, cd in directions:
                q.append([row + rd, col + cd])
        return island
    
    # For DFS, to handle island size, when out of bounds or visited or not land return 0
    # For valid unvisited land, set counter to 0, add return values of all 4 directions
    # Return 1 + this value, as this call is island in itself
    # Mark visited to avoid revisiting.
    # TC: O(M * N), SC: O(M * N)
    # Every cell is visited at most once
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 0:
            return 0
        visited.add((row, col))
        island = 0
        for rd, cd in directions:
            island += dfs(row + rd, col + cd)
        return 1 + island
        
    # Track the maximum size of island for every non visited land call
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                maxArea = max(maxArea, dfs(i, j))

    return maxArea