# Problem: Happy Number
# Topics: Math
# Difficulty: Easy
# Evidence: LeetCode Accepted
# Link: https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n:
                n, digit = divmod(n, 10)
                total += digit * digit
            n = total
        return n == 1
