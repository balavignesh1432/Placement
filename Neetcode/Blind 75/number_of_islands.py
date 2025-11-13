def numIslands(self, grid: List[List[str]]) -> int:    
    # For each 1, perform dfs or bfs and that should not be already visited
    # In DFS, only perform when within bounds, not visited and value is 1, Otherwise return
    # For calling all directions, use displacement array as reduced repeated typing
    # Use Global visited set to keep track of already visited 1s.
    # TC: O(m * n), SC: O(m * n) For Call stack and Visited Set
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    def dfs(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0" or (row, col) in visited:
            return
        visited.add((row, col))
        for rowMove, colMove in directions:
            dfs(row + rowMove, col + colMove)
    
    # In Bfs, push element to queue. 
    # Until the queue becomes empty, deque and then only add neighbors to queue if within bounds, not visited, and value is 1
    # Add the cell to visited
    # TC: O(m * n), SC: O(m * n) For Queue and Visited Set
    def bfs(row, col):
        q = deque()
        q. append([row, col])
        while q:
            r, c = q.popleft()
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                continue    # Use Continue[in BFS] to simulate return in recursion[DFS]
            visited.add((r, c))
            for rd, cd in directions:
                q.append([r + rd, c + cd])

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                bfs(i, j)
                islands += 1
    return islands