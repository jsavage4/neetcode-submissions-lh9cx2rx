class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        lR, lC, rR, rC = 0, 0, height - 1, width - 1
        row = 0
        while lR <= rR:
            midR = (lR + rR) // 2
            if matrix[midR][0] <= target and matrix[midR][len(matrix[midR]) - 1] >= target:
                row = midR
                break
            elif matrix[midR][0] > target:
                rR = midR - 1
            else:
                lR = midR + 1
        while lC <= rC:
            midC = (lC + rC) // 2
            if matrix[row][midC] > target:
                rC = midC - 1
            elif matrix[row][midC] < target:
                lC = midC + 1
            else:
                return True

        return False