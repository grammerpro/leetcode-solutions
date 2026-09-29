# Problem: Single Number
# Topics: Bit Manipulation
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for value in nums:
            result ^= value
        return result
