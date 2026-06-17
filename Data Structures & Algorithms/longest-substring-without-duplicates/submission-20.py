class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        store = set()
        while r<len(s):
            if s[r] in store:
                store.remove(s[l])
                l+=1
            else:
                store.add(s[r])
                r+=1
                res = max(res, r-l)
        return res