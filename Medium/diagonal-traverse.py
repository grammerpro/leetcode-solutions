# Problem: Diagonal Traverse
# Topics: Matrix
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, columns = len(mat), len(mat[0])
        order = []
        for total in range(rows + columns - 1):
            first_row = max(0, total - columns + 1)
            last_row = min(rows - 1, total)
            diagonal = [mat[row][total - row] for row in range(first_row, last_row + 1)]
            if total % 2 == 0:
                diagonal.reverse()
            order.extend(diagonal)
        return order
