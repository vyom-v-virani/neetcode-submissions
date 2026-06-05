class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        store = set()
        max_len = 0
        while r<len(s):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            leng = r-l + 1
            if leng>max_len:
                max_len = leng
            r+=1
        return max_len
                

