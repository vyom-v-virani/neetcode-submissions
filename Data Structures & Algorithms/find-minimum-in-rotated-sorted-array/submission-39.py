class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mini = nums[0]
        while l<=r:
            m = (r+l)//2
            mini = min(mini, nums[m])
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m-1
        return mini