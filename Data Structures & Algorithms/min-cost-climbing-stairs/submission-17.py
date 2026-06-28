class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) ==0:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        dp = [0]*(len(cost)+1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])

        return min(dp[len(cost)-1], dp[len(cost)-2])