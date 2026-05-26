class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return 0
        else:
            dp[0] = 0
            dp[1] = 0
            for i in range(2, len(cost)+1):
                dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(cost)]
