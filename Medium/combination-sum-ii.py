# Problem: Combination Sum II
# Topics: Backtracking
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def extend(start, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            for index in range(start, len(candidates)):
                value = candidates[index]
                if value > remaining:
                    break
                if index > start and value == candidates[index - 1]:
                    continue
                current.append(value)
                extend(index + 1, remaining - value)
                current.pop()

        extend(0, target)
        return result
