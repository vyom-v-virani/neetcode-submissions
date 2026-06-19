class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top<=bot:
            mid = (bot+top)//2
            if matrix[mid][0] > target:
                bot = mid-1
            elif matrix[mid][-1] < target:
                top = mid+1
            else:
                break
        
        if not (top <= bot):
            return False

        l, r = 0, len(matrix[0])-1

        while l<=r:
            m = (r+l)//2
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] > target:
                r = m-1
            else:
                l = m+1
        return False