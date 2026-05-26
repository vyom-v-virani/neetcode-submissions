class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while l<r:
            curScore = numbers[l] + numbers[r]
            if curScore > target:
                r-=1
            elif curScore<target:
                l+=1
            else:
                return [l+1, r+1]
        return []

