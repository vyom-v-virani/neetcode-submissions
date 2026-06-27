class Solution:
    def hammingWeight(self, n: int) -> int:
        test = bin(n)
        count = 0
        for c in test:
            if c == '1':
                count+=1
        return count
