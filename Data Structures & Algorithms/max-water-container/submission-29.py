class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_vol = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            if area>max_vol:
                max_vol = area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_vol
