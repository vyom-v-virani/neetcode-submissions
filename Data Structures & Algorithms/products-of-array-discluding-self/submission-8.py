class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_length = len(nums)
        res = [0] * list_length 
        
        for i in range(list_length):
            prod = 1
            for j in range(list_length):
                if i ==j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res