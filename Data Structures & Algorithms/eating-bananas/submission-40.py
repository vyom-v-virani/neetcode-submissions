class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<=r:
            m = l+((r-l)//2)
            
            total_h = 0
            for p in piles:
                total_h += math.ceil(p/m)
            if total_h<=h:
                res = m
                r=m-1
            else:
                l = m+1
        return res