class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:

            if target == matrix[row][col]:
                return True

            elif target < matrix[row][col]:
                col = col - 1

            else:
                row = row + 1

        return False