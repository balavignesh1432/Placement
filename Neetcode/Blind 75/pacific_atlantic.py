def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # Intuition, since have to find cells both flow into two oceans
    # Start DFS from the ocean cells itself, then keep updating cells for respective oceans from which water can flow
    # Then finally return cells that are in both the sets
    # TC: O(m*n), SC: O(m * n)
    pacific = set()
    atlantic = set()
    rows = len(heights)
    cols = len(heights[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = []

    # Create sets with edge cells added to the appropriate oceans set
    for row in range(rows):
        pacific.add((row, 0))
        atlantic.add((row, cols - 1))
    for col in range(cols):
        pacific.add((0, col))
        atlantic.add((rows - 1, col))
    
    # Base case, check if out of bounds, already visited, or height is not >= its calling cell's height
    # TC: O(m*n), SC: O(m * n)
    def dfs(row, col, parent, visited):
        if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visited or parent > heights[row][col]:
            return  
        visited.add((row, col))
        for rd, cd in directions:
            dfs(row + rd, col + cd, heights[row][col], visited)

    # BFS Using Queue
    # Initially add row, col and parent into queue (Similar to dfs parameters)
    def bfs(row, col, parent, visited):
        q = deque()
        q.append([row, col, parent])
        while q:
            row, col, parent = q.popleft()
            # Base case, check if out of bounds, already visited, or height is not >= its calling cell's height
            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visited or parent > heights[row][col]:
                continue    
            # If valid cell of the graph search, then add to set, and explore neighbors
            visited.add((row, col)) 
            for rd, cd in directions:
                q.append([row + rd, col + cd, heights[row][col]])

    # Perform DFS on Pacific and Atlantics Ocean, only add cells to it if satisfies height condition
    for row, col in list(pacific):
        pacific.remove((row, col))  # As in dfs, bfs function, if already visited, then not performed
        # dfs(row, col, 0, pacific)
        bfs(row, col, 0, pacific)
    for row, col in list(atlantic):
        atlantic.remove((row, col)) # As in dfs, bfs function, if already visited, then not performed
        # dfs(row, col, 0, atlantic)
        bfs(row, col, 0, atlantic)

    # Find the intersection cells both in pacific and atlantic        
    res = list(pacific.intersection(atlantic))
    return [list(cell) for cell in res]