class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sol = [0]*len(cost)


        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0],cost[1])
        else:
            sol[0] = cost[0]
            sol[1] = cost[1]
            for i in range(2, len(cost)):
                sol[i] = min(cost[i]+sol[i-1],cost[i]+ sol[i-2])
        return min(sol[-1], sol[-2])