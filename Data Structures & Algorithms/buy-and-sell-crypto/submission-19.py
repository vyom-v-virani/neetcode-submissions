class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_dif = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > 0 and prices[j]-prices[i] > max_dif:
                    max_dif = prices[j]-prices[i]
        return max_dif