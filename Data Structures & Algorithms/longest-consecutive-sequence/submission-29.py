class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        count = 0
        
        for num in nums:
            streak = 0
            curr = num
            while curr in store:
                streak+=1
                curr+=1
            count = max(count, streak)
        return count
