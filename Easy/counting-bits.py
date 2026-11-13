# Problem: Counting Bits
# Topics: Bit Manipulation
# Difficulty: Easy
# Evidence: LeetCode Accepted
# Link: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        for value in range(1, n + 1):
            counts[value] = counts[value >> 1] + (value & 1)
        return counts
