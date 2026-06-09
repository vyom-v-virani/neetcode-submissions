class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        def addfruit(r, c):
            nonlocal fresh
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] != 1 or (r, c) in visit):
                return
            q.append((r, c))
            visit.add((r, c))
            fresh-=1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0: return 0
        minute = -1 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addfruit(r+1, c)
                addfruit(r-1, c)
                addfruit(r, c-1)
                addfruit(r, c+1)
            minute+=1
        return minute if fresh ==0 else -1
