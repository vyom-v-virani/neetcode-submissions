class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0]*len(temps)

        for i in range(len(temps)):
            for j in range(i+1, len(temps)):
                if temps[j]>temps[i]:
                    res[i] = j-i
                    break
        return res