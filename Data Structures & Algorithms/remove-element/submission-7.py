class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for num in nums:
            if num == val:
                continue
            res.append(num)
        nums[:len(res)] = res
        return len(res)