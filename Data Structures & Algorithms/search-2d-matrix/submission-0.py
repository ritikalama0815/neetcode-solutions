class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, cols = len(matrix), len(matrix[0])

        top, bottom = 0, row - 1

        while top <= bottom:
            mid = (top+bottom)//2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if not top <= bottom:
            return False
        mid = (top+bottom)//2
        left, right = 0, cols - 1
        while left<=right:
            m = (left+right)//2
            if target > matrix[mid][m]:
                left = m+1
            elif target < matrix[mid][m]:
                right = m - 1
            else:
                return True

        return False
        


        