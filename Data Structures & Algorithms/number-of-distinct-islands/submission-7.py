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
                cur_r, cur_c = q.popleft()
                shape.append((cur_r-r, cur_c-c))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == 1):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return tuple(shape) 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    island_shape = bfs(i, j)
                    islands.add(island_shape)
        return len(islands)