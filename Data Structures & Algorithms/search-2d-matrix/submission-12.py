class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bot = 0, row-1
        while top<=bot:
            mid  = top + ((bot-top)//2)
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break
        if not (top<=bot):
            return False
        
        row = top + ((bot-top)//2)
        l, r = 0, col-1

        while l<=r:
            m = l+ ((r-l)//2)
            if target == matrix[row][m]:
                return True
            elif target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
        return False
