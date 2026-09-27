# Problem: Longest Substring Without Repeating Characters
# Topics: Sliding Window
# Difficulty: Medium
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = best = 0
        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)
            seen[char] = right
            best = max(best, right - left + 1)
        return best
