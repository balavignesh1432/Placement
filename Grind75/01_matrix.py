def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    # Intuition, when shorter path beween multiples things, Multisource BFS is used
    # But since in BFS, start with nodes and incrementally spread out, adding depth 1 to curr depth
    # then we can add depth to curr position,
    # So, We start from 0s to reach 1s instead of from 1s to 0s
    # This way update distance matrix as we branch out
    # Initialise distance matrix with 0
    # Add all 0  nodes to queue with distance 0
    # Then pop, and mark visited to avoid repeated work, this ensures each cell is visited only once
    # Store the distance in the separate matrix for the position
    # Now branch out in 4 directions incrementing depth
    # TC: O(M * N), SC: O(M * N)
    # When branching from 0, if encounter 0, no problem, add to queue with depth + 1
    # But that position will be already be in the queue with depth 0 before that, waiting to be processed
    # When it is processed, it will be visited, so depth + 1 call will be rejected
    # When reached 1, still branch out to further may be the shorter distance is through that 1,
    # If not still add to queue, as some shorter distance will be already before in that queue, waiting to be processed
    # So simply, mark the distance matrix with distance
    # IMP: It will only be updated once, as we are using visited, and thus guarantees shortest distance
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    res = [[0] * len(mat[0]) for _ in range(len(mat))]
    q = deque()        
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                q.append([i, j, 0])
    visited = set()
    while q:
        row, col, dist = q.popleft()
        if row < 0 or col < 0 or row >= len(mat) or col >= len(mat[0]) or (row, col) in visited:
            continue
        visited.add((row, col))
        res[row][col] = dist        # Read the IMP section
        for rd, cd in directions:
            q.append([row + rd, col + cd, dist + 1]) 
    return res