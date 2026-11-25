# Problem: Contains Duplicate II
# Topics: Sliding Window
# Difficulty: Easy
# Evidence: LeetCode Accepted
# Link: https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for index, value in enumerate(nums):
            if value in last_seen and index - last_seen[value] <= k:
                return True
            last_seen[value] = index
        return False
