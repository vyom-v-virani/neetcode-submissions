class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        for i in range(len(res)):
            prod = 1
            for j in range(len(res)):
                if i == j:
                    continue
                prod*=nums[j]
            res[i] = prod
        return res