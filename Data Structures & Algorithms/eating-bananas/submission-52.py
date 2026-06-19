class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l<=r:
            m = (r+l)//2
            max_hours = 0
            for p in piles:
                max_hours += math.ceil(float(p)/m)
            if max_hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
