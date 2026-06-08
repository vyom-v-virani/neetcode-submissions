class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        self.max_area = 0

        def bfs(r, c):
            q = collections.deque()
            area = 1
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.pop()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit ):
                        visit.add((nr, nc))
                        q.append((nr,nc))
                        area +=1
            if area > self.max_area:
                self.max_area = area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    bfs(r, c)
        return self.max_area
