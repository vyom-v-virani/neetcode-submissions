class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        for num in nums:
            
            if num<mini:
                mini = num
        return mini