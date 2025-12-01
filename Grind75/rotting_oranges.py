# Intuition: Use BFS to spread the rot from initially rotten oranges to adjacent fresh oranges
# IMP: DFS can not be used here as we need to process all oranges that rot at the same time step together
# This is because we need to compute time taken for all oranges to rot
# Intially, we add all rotten oranges to the queue and count fresh oranges
# Then we perform BFS, at each step we rot adjacent fresh oranges and decrease the fresh count
# To avoid adding already rotten oranges back to the queue, we mark them as rotten (=2) when adding to the queue
# When the queue is empty, if there are still fresh oranges left, return -1
# Edge Case: If there are no fresh oranges at the start, return 0
# Time Complexity: O(N*M) where N is number of rows and M is number of columns in the grid
# Space Complexity: O(N*M) in the worst case for the queue

from collections import deque
def orangesRotting(self, grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    rotten = []
    fresh = 0
    def bfs(rotten, fresh):
        q = deque(rotten)
        minutes = -1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append([r, c])
            minutes += 1      
        return minutes if not fresh else -1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                rotten.append([i, j])
            if grid[i][j] == 1:
                fresh += 1
    
    return bfs(rotten, fresh) if fresh else 0