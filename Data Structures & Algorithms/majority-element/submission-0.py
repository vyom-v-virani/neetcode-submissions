class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count+=1
                if count > (len(nums)/2):
                    return nums[i]
