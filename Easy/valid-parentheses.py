# Problem: Valid Parentheses
# Topics: Stacks
# Difficulty: Easy
# Evidence: Local tests passed
# Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in matching:
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)
        return not stack
