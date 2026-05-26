class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(d) for d in digits)
        num = int(s)+1
        res = []
        for c in str(num):
            res.append(int(c))
        return res