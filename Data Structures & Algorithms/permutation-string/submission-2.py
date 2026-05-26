class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)-1
        sorted_s1 = sorted(s1)
        while r<len(s2):
            if sorted(s2[l:r+1]) == sorted_s1:
                return True
            else:
                r+=1
                l+=1
        return False