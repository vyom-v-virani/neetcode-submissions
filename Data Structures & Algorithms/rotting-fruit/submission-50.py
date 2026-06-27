class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        def addFruit(r, c):
            nonlocal fresh
            if (r<0 or c<0 or r==rows or c==cols or grid[r][c] != 1 or (r, c) in visit):
                return
            visit.add((r, c))
            q.append((r, c))
            fresh-=1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i, j))
                    visit.add((i, j))

        if fresh == 0:
            return 0
        
        minute = 0

        while q and fresh > 0:
            minute += 1
            for i in range(len(q)):
                r, c = q.popleft()

                addFruit(r+1, c)
                addFruit(r-1, c)
                addFruit(r, c+1)
                addFruit(r, c-1)
        return minute if fresh == 0 else -1
