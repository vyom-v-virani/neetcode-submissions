class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        res = []
        for p,s in pairs:
            res.append((target-p)/s)
            if len(res)>=2 and res[-1]<=res[-2]:
                res.pop()
                
        return len(res)