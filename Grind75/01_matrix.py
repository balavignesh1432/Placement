def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    # Intuition, when shorter path beween multiples things, Multisource BFS is used
    # But since in BFS, start with nodes and incrementally spread out, adding depth 1 to curr depth
    # then we can add depth to curr position,
    # So, We start from 0s to reach 1s instead of from 1s to 0s
    # This way update matrix as we branch out
    # Pop, and update distance matrix
    # Now branch out in 4 directions incrementing depth, mark visited to avoid repeated work, this ensures each cell is visited only once
    # TC: O(M * N), SC: O(M * N)
    # When reached 1, still branch out to further may be the shorter distance is through that 1,
    # If not still add to queue, as some shorter distance will be already before in that queue, waiting to be processed
    # So simply, mark the distance matrix with distance
    # IMP: It will only be updated once, as we are using visited, and thus guarantees shortest distance
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()   
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append([i, j, 0])
                    visited.add((i, j))
        while q:
            row, col, dist = q.popleft()
            mat[row][col] = dist
            for rd, cd in directions:
                r = row + rd
                c = col + cd
                if r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0]) or (r, c) in visited:
                    continue
                visited.add((r, c))
                q.append([r, c, dist + 1]) 
        return mat