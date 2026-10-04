# Problem: Two Sum
# Topics: Hash Tables
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            if target - value in seen:
                return [seen[target - value], index]
            seen[value] = index
        return []
