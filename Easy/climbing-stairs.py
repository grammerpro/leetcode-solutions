# Problem: Climbing Stairs
# Topic: Dynamic Programming
# Difficulty: Easy
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # DP iterative approach to avoid recursion overhead and TLE
        if n <= 2:
            return n
        
        first, second = 1, 2
        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third
            
        return second
