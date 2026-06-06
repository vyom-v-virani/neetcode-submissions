class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def helper(list1):
            if len(list1) == 0:
                return 0
            elif len(list1) == 1:
                return list1[0]
            
            dp = [0]*len(list1)
            dp[0] = list1[0]
            dp[1] = max(list1[0], list1[1])

            for i in range(2, len(list1)):
                dp[i] = max(list1[i]+dp[i-2], dp[i-1])
            return dp[-1]

        money1 = helper(nums[:-1])
        money2 = helper(nums[1:])
        return max(money1, money2)