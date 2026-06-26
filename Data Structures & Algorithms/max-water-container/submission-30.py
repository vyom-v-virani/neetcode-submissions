class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_vol = 0
        while l<=r:
            vol = min(heights[l], heights[r]) * (r-l)
            if vol > max_vol:
                max_vol = vol

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max_vol