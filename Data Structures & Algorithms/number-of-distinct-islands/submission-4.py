class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = set()

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            shape = []

            while q:
                curr_r, curr_c = q.popleft()
                shape.append((curr_r - r, curr_c - c))
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in direction:
                    nr, nc = curr_r+dr, curr_c+dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visit.add((nr, nc))
            return tuple(shape)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    island_shape = bfs(i, j)
                    islands.add(island_shape)
        return len(islands)