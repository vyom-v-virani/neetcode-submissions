class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        vol = min(heights[l],heights[r])*(r-l)

        while l<r:
            if heights[r]<=heights[l]:
                r-=1
            else:
                l+=1
            vol = max((min(heights[l],heights[r])*(r-l)), vol)
        return vol