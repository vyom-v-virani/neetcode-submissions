class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp1 = [0] * (len(nums))
        dp2 = [0] * (len(nums))

        dp1[1] = nums[1]
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            if i < len(nums):
                dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
            if i < len(nums) - 1:
                dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        return max(dp1[len(nums)-1], dp2[len(nums)-2])