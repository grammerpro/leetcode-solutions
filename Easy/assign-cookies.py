# Problem: Assign Cookies
# Topics: Greedy
# Difficulty: Easy
# Evidence: LeetCode Accepted
# Link: https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for cookie in s:
            if child < len(g) and cookie >= g[child]:
                child += 1
        return child
