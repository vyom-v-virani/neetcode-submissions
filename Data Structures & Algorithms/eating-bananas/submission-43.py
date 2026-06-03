class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)
        while l<=r:
            m = (r+l)//2
            total_time = 0
            for i in range(len(piles)):
                total_time += math.ceil(piles[i]/m)
            if total_time <= h:
                res = min(res, m)
                r = m-1
            elif total_time > h:
                l = m+1
        return res
            

