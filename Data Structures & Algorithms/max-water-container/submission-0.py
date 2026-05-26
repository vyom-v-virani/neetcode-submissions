class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if min(heights[i], heights[j])*(j-i)>max_vol:
                    max_vol = (min(heights[i], heights[j])*(j-i))
        return max_vol
