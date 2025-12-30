def solve(self, board: List[List[str]]) -> None:
    # Multisource BFS: Since edge of board Os can not be surrounded by X,
    # Any island that can be formed with edges will never be surrounded
    # So add all edge "0"s into the queue and perform multisource BFS
    # Marking island cells as visited
    # Finally iterate to cells with "O" but not visited
    # These could be surrounded by "X", so mark all of them "X"
    # TC: O(M * N), SC: O(M * N)
    # Each cell is visited at most 1
    
    q = deque()
    visited = set()
    for i in range(len(board)):
        if board[i][0] == "O":
            q.append([i, 0])
        if board[i][-1] == "O":
            q.append([i, len(board[0]) - 1])

    for j in range(len(board[0])):
        if board[0][j] == "O":
            q.append([0, j])
        if board[-1][j] == "O":
            q.append([len(board) - 1, j])

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def bfs():
        while q:
            row, col = q.popleft()    
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] == "X":
                continue
            visited.add((row, col))
            for rd, cd in directions:
                q.append([row + rd, col + cd])
    bfs()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O" and (i, j) not in visited:
                board[i][j] = "X"