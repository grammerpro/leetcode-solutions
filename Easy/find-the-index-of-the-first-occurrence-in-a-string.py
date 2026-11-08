# Problem: Find the Index of the First Occurrence in a String
# Topics: Strings
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
