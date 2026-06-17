class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        store = set(nums)
        for num in nums:
            curr = num
            streak = 0
            while curr in store:
                streak+=1
                curr+=1
            max_streak = max(streak, max_streak)
        return max_streak
