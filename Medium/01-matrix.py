# Problem: 01 Matrix
# Topics: Graphs
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/01-matrix/

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        distance = [[-1] * columns for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for column in range(columns):
                if mat[row][column] == 0:
                    distance[row][column] = 0
                    queue.append((row, column))
        while queue:
            row, column = queue.popleft()
            for next_row, next_column in ((row + 1, column), (row - 1, column),
                                          (row, column + 1), (row, column - 1)):
                if (0 <= next_row < rows and 0 <= next_column < columns
                        and distance[next_row][next_column] == -1):
                    distance[next_row][next_column] = distance[row][column] + 1
                    queue.append((next_row, next_column))
        return distance
