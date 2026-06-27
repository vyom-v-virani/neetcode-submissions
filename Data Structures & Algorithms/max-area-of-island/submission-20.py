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
                cur_r, cur_c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = cur_r + dr, cur_c + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        q.append((nr, nc))
                        area+=1
            
            if area > self.max_area:
                self.max_area = area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    bfs(i, j)
        return self.max_area