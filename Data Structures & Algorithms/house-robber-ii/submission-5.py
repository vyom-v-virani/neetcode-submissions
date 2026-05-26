class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp1 = [0] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        dp2 = [0] * (len(nums) - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], nums[i]+ dp1[i-2])
        for j in range(2, len(nums)-1):
            dp2[j] = max(dp2[j-1], nums[j+1] + dp2[j-2])
        
        return max(dp1[-1], dp2[-1])
            
