class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                if nums[l] + nums[r] == target:
                    return [l, r]