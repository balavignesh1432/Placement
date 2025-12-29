def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    # Multi Source BFS: Without using visited set
    # Since 0 is chest to be found, distance for each cell to 0
    # Distance to 0 itself is 0
    # So start from 0, as sources, Add to q with 0 distances
    # Now perform BFS traversal, adding 1 to distance for each level increment
    # If out of bounds, or already visited (Not Infinity) or not traversable (-1), continue
    # Otherwise, update the distance for that traversable cell
    # TC: O(M * N), SC: O(M * N)
    # Since each cell is visited at most once, for which shortest distance is first found
    q = deque()
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                q.append([i, j, 0])
    def bfs():
        while q:
            row, col, d = q.popleft()
            for rd, cd in directions:
                r = row + rd
                c = col + cd
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 0x7FFFFFFF or grid[r][c] == -1:
                    continue
                grid[r][c] = d + 1
                q.append([r, c, d + 1])
    bfs()