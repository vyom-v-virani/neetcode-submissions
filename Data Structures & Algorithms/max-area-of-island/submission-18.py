class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        self.max_area = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row+dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] ==1):
                        area +=1
                        visit.add((nr, nc))
                        q.append((nr, nc))
            if area>self.max_area:
                self.max_area = area
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    bfs(i, j)

        return self.max_area