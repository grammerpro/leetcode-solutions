# Problem: Contains Duplicate
# Topics: Hash Tables
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
