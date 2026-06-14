class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l<=r:
            m = (l+r)//2
            k = 0
            for i in range(len(piles)):
                k+=math.ceil(piles[i]/m)
            if k<=h:
                res = m
                r = m-1
            else:
                l = m+1
        return res