class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for num in nums:
            if num in res:
                continue
            else:
                res.append(num)
        return len(res)!=len(nums)