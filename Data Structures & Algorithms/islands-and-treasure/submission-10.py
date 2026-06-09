class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()

        def addroom(r, c):
            if (r<0 or c<0 or r>=rows or c>=cols or (r, c) in visit or grid[r][c] == -1):
                return
            grid[r][c] = distance+1
            visit.add((r, c))
            q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addroom(r+1, c)
                addroom(r-1, c)
                addroom(r, c+1)
                addroom(r, c-1)
            distance+=1