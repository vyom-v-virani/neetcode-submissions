class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for i in range(len(nums)):
            count, curr = 0, nums[i]
            while curr in store:
                count +=1
                curr += 1
            res = max(res, count)
        return res