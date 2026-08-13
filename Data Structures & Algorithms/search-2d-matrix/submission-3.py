class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols

            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                high = mid - 1
            else:
                low = mid + 1
        return False
