class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        max_count = 0
        store = set()
        while r < len(s):
            if s[r] not in store:
                store.add(s[r])
                r += 1
                if (r - l) > max_count:
                    max_count = r - l
            else:
                store.remove(s[l])
                l += 1
        return max_count
