# Problem: Game of Life
# Topics: Matrix
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, columns = len(board), len(board[0])
        previous = [row[:] for row in board]
        for row in range(rows):
            for column in range(columns):
                neighbors = 0
                for near_row in range(max(0, row - 1), min(rows, row + 2)):
                    for near_column in range(max(0, column - 1), min(columns, column + 2)):
                        neighbors += previous[near_row][near_column]
                neighbors -= previous[row][column]
                if previous[row][column]:
                    board[row][column] = 1 if neighbors in (2, 3) else 0
                else:
                    board[row][column] = 1 if neighbors == 3 else 0
