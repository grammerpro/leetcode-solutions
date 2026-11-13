# Problem: Combination Sum
# Topics: Backtracking
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        answer = []
        current = []

        def build(start, remaining):
            if remaining == 0:
                answer.append(list(current))
                return
            for index in range(start, len(candidates)):
                value = candidates[index]
                if value > remaining:
                    break
                current.append(value)
                build(index, remaining - value)
                current.pop()

        build(0, target)
        return answer
