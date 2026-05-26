class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1] * (amount)
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[-1] if dp[amount]<= amount else -1