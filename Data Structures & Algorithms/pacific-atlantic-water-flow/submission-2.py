class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevheight):
            if (r<0 or c<0 or r==rows or c==cols or (r, c) in visit or grid[r][c] < prevheight):
                return
            visit.add((r, c))
            dfs(r+1, c, visit, grid[r][c])
            dfs(r-1, c, visit, grid[r][c])
            dfs(r, c+1, visit, grid[r][c])
            dfs(r, c-1, visit, grid[r][c])

        for r in range(rows):
            dfs(r, 0, pac, grid[r][0])
            dfs(r, cols-1, atl, grid[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, pac, grid[0][c])
            dfs(rows-1, c, atl, grid[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res