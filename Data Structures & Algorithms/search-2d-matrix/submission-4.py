class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        row=len(matrix[0])
        right=len(matrix) * row - 1

        while left <= right:
            index = (left + right) // 2
            value = matrix[index // row][index % row]
            if value == target: return True
            elif value > target: right = index - 1
            else: left = index + 1
        
        return False
        